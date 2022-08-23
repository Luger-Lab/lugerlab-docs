Computers
=========

Storage - Where should I store?
-------------------------------

.. toctree::
   :maxdepth: 2

   petalibrary
   workstations
   external_hard_drives
   bio06_server
   biokem_storage
   google_drive

As EM produces massive amounts of data, storage is an ever present issue. Hold
onto the raw images and analysis protocol. Interm data should be made and
cleaned up as frequently as possible to avoid running out of storage space.

Active EM data
^^^^^^^^^^^^^^
Petalibrary: This is the first place it will be stored, coming off collection
and preprocessing. You can then keep it here and process it with BioKEM cluster
resources or mount it to one of our workstations.

Local workstations: The only other place active EM data should be stored is on
our local workstations. Do not transfer is here via an external HDD, use an
``rsync`` or ``scp`` command.

**Do not store active data on an external HDD.**

Processed data that I might come back to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Petalibrary: Store these data on Petalibrary until you are sure they are fully
processed and published or won't ever be.

Terminal data (fully processed and published or will never be)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
External HDD: Move these from Petalibrary to an external HDD and make sure to
fill out the form and properly label them.

Computing resources - Where should I compute?
---------------------------------------------

.. toctree::
   :maxdepth: 2

   computers/local_workstations
   computers/biokem_cluster
   computers/other_clusters
   computers/cumulus

On-the-fly preprocessing
^^^^^^^^^^^^^^^^^^^^^^^^
**BioKEM cluster** For real time motion correction, 2D and 3D classification off
the Krios (or F20/30, if you can get Gary to push your data from the detector to
Petalibrary) we will use the BioKEM cluster.

- Start up the auto-transfer protocol to move images from the camera to BioKEM-storage to the lab's Petalibrary deposit folder.
- Start an interactive job on the OTF node to run RELION inside the deposit folder.
- **OR** use CUmulus to launch a CryoSPARC Live session which will schedule jobs onto the OTF node.

Data processing
^^^^^^^^^^^^^^^
**BioKEM cluster** After collection, data processing can continue right from
Blanca, however you will no longer use the OTF node, simply schedule jobs using
SBGrid applications or CryoSPARC through CUmulus onto any of the other BioKEM
nodes or schedule preemptible jobs on other Blanca nodes.

- Faster
- Access to more resources
- Don't have to deal with moving data
- Secure

**Local workstations** You can also continue processing your data on our local
workstations. To do this, either ``rsync`` or ``scp`` your data from Petalibrary
onto one of the workstations, making sure you have reserved it for processing.
Another option is to mount Petalibrary directly to the workstation using a
``mount`` command (this may already be handled in the fstab file).

- Don't have to submit to queue
- Don't have explain concept of HPC
- No wall clock limits

Molecular dynamics simulations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Local workstations** The advantage of running simulations on our workstations
is that you can let the simulations run in the background forever, assuming
you've reserved the computer. The disadvantage is that you will only have access
to ~4 lower grade GPUs at a time. This can be fine for many applications. An
advantage is that MD software is probably already installed and maintained.

**Other clusters (Fiji, Summit, Apline, Xsede)** For large simulation runs a
cluster is a great choice. Fijis GPUs are slow, but underutilized. Summit has
many slower GPUs. Apline will be a great choice once it is operational. If you
can get an Xsede allocation, that is probably the best place to do this. One
other place to consider is D.E. Shaw's Anton, however you will need to apply for
a run and it will likely only be a few super long simulations. BioKEM cluster is
not the place to run simulations, unless you run them preemptible.
