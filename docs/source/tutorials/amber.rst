AMBER
=====

Adapted from `AMBER tutorial <https://ambermd.org/tutorials/basic/tutorial15/index.php>`_.
Read the full `manual <https://ambermd.org/doc12/Amber22.pdf>`_. 
See `github <https://github.com/Luger-Lab/MD-simulations>` for exmple scripts.

Introduction
~~~~~~~~~~~~

.. image:: amber_workflow.png
   :width: 300
   :align: right

AMBER is a suite of molecular dynamics programs that can be used to simulate
biomolecules at a variety of granularities. It is broken into two main parts.
AMBERTools, which includes the free-to-use MD engine, ``sander`` which runs on 
CPUs, as well as various analysis scripts. And AMBER, which is distributed 
through a license and includes the GPU-accelerated engine, ``pmemd``. We will
be using the ``pmemd`` version of the software.

All-atom with explicit solvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most common (and likely accurate) type of simulation is all-atom with 
explicit solvent. In this simulation, all atoms, including solvent molecules
are simulated as discrete points. 

Prepare structure
-----------------

The first step to any simulation is to acquire a starting structure. We will 
usually start from a PDB, either a solved structure, one you've modelled, or 
one that you've built. Things to consider with making a starting structure:

   -  the larger the system the longer the simulation steps will take
   -  clashes need to be resolved or they will cause failures later
   -  most of the time, it's best to remove 5' phosphates from DNA 

For this tutorial, we will start from a github repo (clone this in your PL)

   .. code-block:: bash
      biokem-interactive
      cd <test_location>
      git clone git@github.com:Luger-Lab/MD-simulations.git

This repo is organized first by type of simulation, type of solvent, where 
this simulation will run, and finally by replicate number. When running this for real,
clone a new repo and then copy the ``rep0`` directory into one with the unique
identifier of your simulation. But for now, navigate to the 
``all_atom/explicit_solvent/blanca/rep0``:

   .. code-block:: bash
      
      cd MD-simulations/all_atom/explicit_solvent/blanca/rep0

If you ``ls`` this directory, you should see all of the necessary directories for 
running a simulation:

   -  analysis: contains scripts and is a place to run/store analysis
   -  mdinfo: empty, but will contain simple information about your run
   -  outputs: empty, but will contain detailed information about your run
   -  pdb_prep: contains example pdb, get your structure ready here
   -  restarts: empty, but will contain snapshots used to "restart" simulations
   -  scripts: contains most of the scripts you will need to run
   -  trajectories: empty, but will contain the actual data files 

Navigate to the ``pdb_prep`` directory and open the example pdb:

   .. code-block:: bash

      cd pdb_prep
      sbgrid 
      chimerax atg.pdb

You should see a simple three basepair DNA strand. With your own starting structure, 
now is the time to resolve clashes, remove any 5' phosphates, and make sure residues
are named properly (DNA needs to be DA, DC, DT, DG). But we will exit
ChimeraX and prep the pdb. We will load the AMBER module and use a contained program
to reduce the system, remove waters, and put the file in the correct format. Although
this step isn't always necessary, it's usually helpful.

   .. code-block:: bash
      
      ml amber
      pdb4amber -i atg.pdb -o atg_amber.pdb --reduce --dry 

If there were no errors, the output should say so and should have created a number of 
files. We can now add enough ions to the system to neutralize it (a non-neutral system
creates potentials which are often to large to calculate). We will need to edit this file:

   .. code-block:: bash

      #load forcefield parameters
      source leaprc.protein.ff14SB  
      source leaprc.DNA.bsc1
      source leaprc.water.tip3p

      unit = loadpdb <name>.pdb 
      #'loadpbd' fills in missing H atoms, and missing heavy atoms

      #add counter-ions
      addions unit Cl- 0
      addions unit K+ 0

      #save neutralized PDB
      savepdb unit <name>_neutralized.pdb

      quit

In this file, we will load the various forcefields we need (there are other forcefields for
different molecules, as well as different versions of each). We will then load our pdb, add
counterions and save the pdb. Edit this file with the correct input and output filenames:

   .. code-block:: bash

      nano ../scripts/0_neutralize.leap

You can now run the file using a program called ``tleap`` (from ``pdb_prep``):

   .. code-block:: bash
      
      tleap -sf ../scripts/0_neutralize.leap

If all goes well, you should get 0 errors and a readout telling which ions were placed.

We will now edit the next scripts and look at how many water molecules we need to 
solvate our box:

   .. code-block:: bash
      
      nano ../scripts/1_addwater.leap

   .. code-block:: bash

      tleap -sf ../scripts/1_addwater.leap

We can take the number of residues add (waters) and run:

   .. code-block:: bash

      python ../scripts/2_salt_concentration.py --wat <waters> --conc <molarity_of_salt>

You can place the output of this into the next script (don't forget to edit the names
and box size as well):

   .. code-block:: bash

      nano ../scripts/3_addions.leap 

Run with ``tleap``:

   .. code-block:: bash

      tleap -sf ../scripts/3_addions.leap

To speed up the simulation we will reparition the mass of hydrogen atoms, which 
allows us to run longer time steps.

   .. code-block:: bash

      parmed -p nhmrp_atg_buffer.prmtop

   .. code-block:: bash

      HMassRepartition

   .. code-block:: bash

      outparm ../atg_buffer.prmtop
      quit


Minimization
------------

Now we have prepared our system and can run a minimization step to relieve any
atom placements that may cause problems later. We will run the rest of our scripts
from the ``scripts`` directory:

   .. code-block:: bash

      cd ../scripts

We will use two input files to run minimization:

``min1.in``:

   .. code-block:: bash

      Minimization 1
      &cntrl
      imin=1,maxcyc=5000,irest=0,ntx=1,
      ntpr=5,
      ntr=1, restraint_wt=10.0,restraintmask='(!:WAT,Cl-,Na+,NA,CL,K+,K)&!(@H=)',
      cut=10.0,ntt=3,gamma_ln=3,temp0=10.0,
      ntb=1,iwrap=1,
      /

      &ewald
      vdwmeth=1,order=4,dsum_tol=0.000001,netfrc=0,eedmeth=1,
      /

``min2.in``:

   .. code-block:: bash

      Minimization 2
      &cntrl
      imin=1,maxcyc=5000,irest=0,ntx=1,
      ntpr=5,
      cut=10.0,ntt=3,gamma_ln=3,temp0=10.0,
      ntb=1,iwrap=1,
      /
      
      &ewald
      vdwmeth=1,order=4,dsum_tol=0.000001,netfrc=0,eedmeth=1,
      /

In the first minimization we are restraining anything that isn't part of the 
buff to allow the buffer to disperse in the box. In the second, we are allowing
the whole system to disperse. We will run this script on the cluster with (you
will need to edit and fill in the name of your system):

``4_blanca_minimization.q``:

   .. code-block:: bash

      #!/bin/bash
      #SBATCH --partition=blanca-biokem
      #SBATCH --qos=blanca-biokem 
      #SBATCH --account=blanca-biokem
      #SBATCH --job-name=minimization
      #SBATCH --nodes=1
      #SBATCH --ntasks=50
      #SBATCH --mem=128gb
      #SBATCH --time=24:00:00
      #SBATCH --output=/home/%u/slurmfiles_out/slurm_%j.out
      #SBATCH --error=/home/%u/slurmfiles_err/slurm_%j.err

      module load amber/v22
      NAME=''

      #run the first minimization
      mpirun -np 50 pmemd.MPI -O -i min1.in -o ../outputs/min1.out -p ../${NAME}_buffer.prmtop -c ../${NAME}_buffer.inpcrd -r ../restarts/${NAME}_min1.rst\
      -x ../trajectories/${NAME}_min1.nc -inf ../mdinfo/${NAME}_min1.mdinfo -ref ../${NAME}_buffer.inpcrd

      #run the second minimization
      mpirun -np 50 pmemd.MPI -O -i min2.in -o ../outputs/min2.out -p ../${NAME}_buffer.prmtop -c ../restarts/${NAME}_min1.rst -r ../restarts/${NAME}_min2.rst\
      -x ../trajectories/${NAME}_min2.nc -inf ../mdinfo/${NAME}_min2.mdinfo

Run these minimizations on the cluster:

   .. code-block:: bash

      sbatch 4_blanca_minimization.q

You can check the progress of the run by reading the files in ``mdinfo`` and ``outputs``.




Heating
-------


Equilibration
-------------


Production
----------


Analysis
--------

All-atom with implicit solvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prepare structure
-----------------
Preparing structures with implicit solvents requires that we use the ``igb=8`` parameter
as well as remove the periodic box argument. Because we aren't using solvent, 
we also don't need to solvate the system. 

Minimization
------------
Minimization is done like explicit solvents, simply keep the above parameters in mind.

Heating
-------
Heating is done like explicit solvents, simply keep the above parameters in mind.

Equilibration
-------------
Equilibration is done like explicit solvents, simply keep the above parameters in mind.

Production
----------
Production is done like explicit solvents, simply keep the above parameters in mind.

Analysis
--------

Coarse-grained (implicit solvent)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prepare structure
-----------------


Minimization
------------


Heating
-------


Equilibration
-------------


Production
----------


Analysis
--------