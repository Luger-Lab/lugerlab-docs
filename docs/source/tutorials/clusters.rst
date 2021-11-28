[Return to the How Computers Work mainpage](https://luger-lab.github.io/coding-tutorials/basic_computing_computers/)

## [&larr; Back to Storage](https://luger-lab.github.io/coding-tutorials/basic_computing_computers/storage/)

## Description
In order to do complicated and large scale compute jobs, institutions, universities, and companies build computing clusters that aggregate high performance computing machines in one place and allocate their use to maximize efficiency.  
0. *General structure.* Compute clusters like the ones housed at the University of Colorado ([Fiji](https://bit.colorado.edu/biofrontiers-computing/fiji/fiji-user-guide/), [Summit](https://www.colorado.edu/rc/resources/summit), [Blanca](https://www.colorado.edu/rc/resources/blanca)) are managed by central organization that house and maintain the hardware components of these computers in large server racks.![cluster](cluster.jpg)
    0. *Nodes.* Clusters are divided up into nodes, that are physically connected resources and allow users fast data transfer when executing a job. Users are rarely confined to using a single node per job and can also share nodes with other, if enough resources exist to run multiple jobs at once.
    0. *Mass storage.* Attached to these clusters is usually a mass storage server like [Petalibrary](https://www.colorado.edu/rc/resources/petalibrary), which are connected to the compute nodes through internal ethernet connections which allow data transfer speeds much faster than over the internet or some other connection.
0. *Benefits.*
    - Access to lots of computing resources
    - Often faster/higher grade computers
    - Efficient use of resources
    - Managed by experts
0. *Drawbacks.*
    - Can be expensive
    - Limited control of how the system is set up

## [Back to Tutorials mainpage](https://luger-lab.github.io/coding-tutorials/)
