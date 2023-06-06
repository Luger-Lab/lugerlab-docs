Opentrons OT-2 liquid handling robot
====================================

Goal
----
Learn how to setup the robot, interpret code, and edit global varibales. This tutorial 
will not cover how to write indepth code, as that requires lots of Python knowledge.
Check the `Opentrons website <https://opentrons.com/>`_ for full details.
    
    - :ref:`Operating instructions`
    - :ref:`Robot layout`
    - :ref:`Labware`
    - :ref:`Opentrons app`
    - :ref:`Code basics`

.. _Operating instructions:

Operating instructions
----------------------

    #. Turn on PC 
    #. Open :ref:`Opentrons app`
    #. Turn on robot
    #. Load program (may need to edit and re-import, if changes are desired)
    #. Check for labware offsets
    #. Place labware in specified positions 
    #. Run program 
    #. Clean up labware
    #. Empty tips
    #. Turn off robot
    #. Shut PC

.. _Robot layout:

Robot layout
------------
The OT-2 robot consists of:

    - A deck: 12 slots for various labware. 
    - Robotic arm: 2 slots for pipettes, which can be changed out.
    - Onboard computer: A RaspberryPi running a locked OS.
    - Additonal modules: Heatblock, magnetic, thermocycler, shaker, HEPA.
    - Additional sensors: Camera and door sensor. 

.. _Labware:

Labware
-------
For the robot to operate, it has to know the proper dimensions of everything
in the robot. These dimensions are defined as ``labware`` and there are a 
bunch of presets on the `Opentrons website <https://labware.opentrons.com/?_gl=1*k7s3fb*_ga*NDA4OTUxMzI1LjE2ODU2MzkwMzc.*_ga_66HK7MC5D7*MTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDE4Mi42MC4wLjA.*_ga_GNSMNLW4RY*MTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDE4Mi42MC4wLjA.>`_.
Custom labware can also be added, but should be done so carefully. Some labware
may require an offset or remapping of the labware definition. 

    - Pipettes
    - Tips
    - Plates
    - Troughs
    - Specials

.. _Opentrons app:

Opentrons app
-------------
The Opentrons app is how you interface with the robot. You can:

    - Import protocols
    - See discriptions and layouts
    - View labware definitions
    - Start runs
    - Monitor runs
    - Pause or cancel runs

.. _Code basics:

Code basics
-----------
