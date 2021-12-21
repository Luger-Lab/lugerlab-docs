How to make a structure viewer VM
=================================
.. raw:: html

    <embed>
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
      </head>
      <body>
        <script src="https://3Dmol.org/build/3Dmol-min.js" async></script>
          <div id="container-01"; style="height: 100vh; width: 100%; position: relative;" class='viewer_3Dmoljs' data-href='1aoi.pdb' data-backgroundcolor='0xffffff' data-style='cartoon' ></div>       
      </body>
    </html>
    </embed>

Goal
----
Use a virtual machine to host a webpage that servers 3D structure viewers you
can then embed in talks using a QR code.

Prerequisites
-------------
#. A PDB file (or accession code) of your structure
#. Access to CUmulus (or other cloud computing service, but instructions may differ)
#. Some basic HTML knowledge

Protocol
--------
#. Create a new private network on CUmulus (with associated subnetwork)
#. Create a router to route traffic to scinet-public
#. Attach your new private network interface to the router
#. Spawn a new virtual machine (or clone instance from working volume)

   - CentOS7 operating system, with 16GiB (or less)
   - Because we are just hosting a static webserver an m5.small should be fine
   - Add it to your new network
   - select the security groups required (probably at least default, http, https, and ssh-restricted)
   - add your devices' public key to the key pair (can't access VM without)
   - launch the instance

#. Allocate and associate a floating IP from scinet-public
#. Edit port security groups to match instance 
#. You should now be able to access your VM
#. ``ssh centos@<your.floating.ip.address>`` 

   - accept new fingerprint
   - will access VM as root, if your key pair is valid

#. If you cloned your VM, you should be able to use ``sudo systemctl start httpd`` to start your website

   - put new htmls (or files) in ``/var/www/html/<virtual-host>`` (store sensative data in a different directory and link to it from within html) 
   - access new website at ``http://<your-scinet-public-ip>/<your-file.html>`` 

#. If you didn't clone your VM, install Apache:

   - ``sudo yum install httpd``
   - ``sudo systemctl start httpd``
   - see if it's running: ``sudo systemctl status httpd``

#. Create a virtual host `try here <https://www.tutorialspoint.com/how-to-setup-virtual-hosts-with-apache-web-server-on-linux>`_
#. Add files to your virtual host
#. You can then make structure viewer using `3Dmol.js <https://3dmol.csb.pitt.edu/>`_
#. Basic example of an html file using this:

.. code-block:: html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
     <title>Shawn's biophys talk</title>
   </head>
   <body>
     <script src="https://3Dmol.org/build/3Dmol-min.js" async></script>     
       <div id="container-01"; style="height: 100vh; width: 100%; position: relative;" class='viewer_3Dmoljs' data-href='1aoi.pdb' data-backgroundcolor='0xffffff' data-style='cartoon' ></div>       
   </body>
   </html>


   - where ``data-href='1aoi.pdb'`` can be swapped out for any pdb file or you can use an accession (see `documentation <https://3dmol.csb.pitt.edu/>`_)
   - can also modify colors and styles

#. Lastly, you can make a QR code by simple typing ``qr code <http://your.floating.ip.address/your-file.html>`` into Google and saving the image

