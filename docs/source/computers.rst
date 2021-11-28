Computers
=========

Storage
-------
As EM produces massive amounts of data, storage is an ever present issue. **Hold onto the raw images and analysis protocol.** Interm data should be made and cleaned up as freque$

Where should I store?
~~~~~~~~~~~~~~~~~~~~~
### Active EM data
Petalibrary: This is the first place it will be stored, coming off collection and preprocessing. You can then keep it here and process it with BioKEM cluster resources$

Local workstations: The only other place active EM data should be stored is on our local workstations. Do not transfer is here via an external HDD, use an `rsync` or `$

**Do not store active data on an external HDD.**

### Processed data that I might come back to
Petalibrary: Store these data on Petalibrary until you are sure they are fully processed and published or won't ever be.

### Terminal data (fully processed and published or will never be)
External HDD: Move these from Petalibrary to an external HDD and make sure to fill out the form and properly label them.

.. toctree::
   :maxdepth: 2

   petalibrary
   workstations
   external_hard_drives
   bio06_server
   biokem_storage
   google_drive

Computing resources
-------------------
## Where should I compute?
### On-the-fly preprocessing
**&rarr; BioKEM cluster** For real time motion correction, 2D and 3D classification off the Krios (or F20/30, if you can get Gary to push your data from the detector to Petalibr$
- Start up the auto-transfer protocol to move images from the camera to BioKEM-storage to the lab's Petalibrary deposit folder.
- Start an interactive job on the OTF node to run RELION inside the deposit folder.
- **OR** use CUmulus to launch a CryoSPARC Live session which will schedule jobs onto the OTF node.

### Data processing
**&rarr; BioKEM cluster** After collection, data processing can continue right from Blanca, however you will no longer use the OTF node, simply schedule jobs using SBGrid applic$
- Faster
- Access to more resources
- Don't have to deal with moving data
- Secure

**&rarr; Local workstations** You can also continue processing your data on our local workstations. To do this, either `rsync` or `scp` your data from Petalibrary onto one of th$
- Don't have to submit to queue
- Don't have explain concept of HPC
- No wall clock limits

### Molecular dynamics simulations
**&rarr; Local workstations** The advantage of running simulations on our workstations is that you can let the simulations run in the background forever, assuming you've reserve$

**&rarr; Other clusters (Fiji, Summit, Apline, Xsede)** For large simulation runs a cluster is a great choice. Fijis GPUs are slow, but underutilized. Summit has many slower GPU$

.. toctree::
   :maxdepth: 2
   
   local_workstations
   biokem_cluster
   other_clusters
   cumulus
