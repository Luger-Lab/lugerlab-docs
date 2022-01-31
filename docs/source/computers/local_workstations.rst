Local workstations
==================

We have four local workstations in lab, each equipped with 40CPUS, 4GPUS, and >50TB of storage.

Gaining access to our workstations:

#. Have the tech person send email to BIT asking to create a user for you on all four workstations.
#. Install `CU-Boulder's VPN <https://oit.colorado.edu/services/network-internet-services/vpn>`_
#. Connect to the terminal:

   - Mac/Linux users

    #. Open the `Terminal` app or a terminal emulator
    #. `ssh <username>@<hostname>.int.colorado.edu` (see tech person for hostnames)
    #. Enter password (the cursor will not advance, but you can backspace, if you think you entered it wrong)
    #. Press `Enter`, you should now be connected to the workstation's terminal

   - Windows users

    #. Install `PuTTY <https://www.microsoft.com/en-us/p/putty-unofficial/9n8pdn6ks0f8?activetab=pivot:overviewtab>`
    #. In the ``Host Name (or IP Address)`` section, enter the <hostname> to one of the Workstations
    #. Make sure the ``Port`` is set to ``22``
    #. Select ``SSH`` as the ``Connection Type``
    #. ``Save`` the session for future use (if it isn't prepopulated next time you can load the session)
    #. Then click ``Open``
    #. Enter your username in the new dialog window, press ``Enter``
    #. Enter your password when prompted and press ``Enter`` you should not be connected to the workstation's terminal

#. Starting a remote desktop:

   - Mac users

    #. Log onto the workstation you want to use through a terminal execute:
      - ``echo "xfce4-session" > ~/.Xclients``
      - ``chmod a+x ~/.Xclients``

    #. Install the ``Microsoft Remote Desktop`` app from the App Store
    #. Open the ``Microsoft Remote Desktop`` app
    #. Click on the ``+`` drop-down menu and select ``Add PC``
    #. In the ``PC name`` section, enter the <hostname> of the desired workstation
    #. Click on the ``User account`` drop-down menu and select ``Add User Account...``
    #. Enter your <username> and <password> and click ``Add``
    #. Enter a ``Friendly name`` for the workstation, if desired.
    #. Click ``Add``
    #. Now you should now see a new box associated with the workstation you added
    #. Double click on the box to open the connection
    #. Accept the warning message to continue
    #. A remote desktop should open once the connection is established

   - Windows users

    #. Log onto the workstation you want to use through a terminal execute:
      - ``echo "xfce4-session" > ~/.Xclients``
      - ``chmod a+x ~/.Xclients``
    #. Search the search bar for the ``Remote Desktop Connection`` app, click to start
    #. Enter the designated <hostname> for the ``Computer``
    #. Click ``Connect``
    #. Click ``Yes`` for the security question
    #. A login window should pop up, login with your identikey credentials

   *Mate and Gnome desktops may be available as well, simply use
   ``echo "mate-session" > ~/.Xclients`` or ``echo "gnome-session" > ~/.Xclients``
   instead of the above command.
