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
Protocols for the Opentrons robot are written in Python. An easy tool to help 
you start can be found in the `Protocol Designer <https://designer.opentrons.com/?_gl=1*1te4djx*_ga*NDA4OTUxMzI1LjE2ODU2MzkwMzc.*_ga_66HK7MC5D7*MTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDE4Mi42MC4wLjA.*_ga_GNSMNLW4RY*MTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDE4OC41NC4wLjA.>`_.
Premade protocols can be found in the `Protocol Library <https://protocols.opentrons.com/?_gl=1%2a1ggam66%2a_ga%2aNDA4OTUxMzI1LjE2ODU2MzkwMzc.%2a_ga_66HK7MC5D7%2aMTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDE4Mi42MC4wLjA.%2a_ga_GNSMNLW4RY%2aMTY4NjA2NDE4Mi4yLjAuMTY4NjA2NDU0Ny42MC4wLjA.>`_.
Use either of these methods as starting points. You can use the `Python API <https://docs.opentrons.com/v2/>`_ 
to implement fancier methods or see full descriptions of functions. Functional 
scripts from our lab can be found on `Github <https://github.com/Luger-Lab/Otto_the_Robot>`_.

The basic Opentrons protocol has these parts:

    - Import packages: need to import ``from opentrons import protocol_api`` and other used packages
    - Metadata: information about the protocol that the App will display. Rename here if editing existing script.
    - ``run`` function: must be ``def run(protocol):``
    - ``setup`` function: sets up labware for use later
    - Functions for each task: titrate, plate, make buffs, etc.

Here's an example script:

.. _python:

  from opentrons import protocol_api
  import time
  import sys
  import math
  import random
  import subprocess


  metadata = {
      'protocolName': 'Protein titration - 24 well',
      'author': 'Shawn Laursen',
      'description': '''Put mixes (50ul of protein+dna) and 2x250ul of (dna) next to
                        each other in 96 well plate
                        Titrates protein in 384well. ''',
      'apiLevel': '2.11'
      }

  def run(protocol):
      well_96start = 6 #index from 0

      protocol.set_rail_lights(True)
      setup(2, well_96start, protocol)
      for buff in buffs:
          protein_titration(buff, protocol)
      protocol.set_rail_lights(False)

  def setup(num_buffs, well_96start, protocol):
      #equiptment
      global tips300, plate96, plate384, p300m, tempdeck
      tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
      plate96 = protocol.load_labware('costar_96_wellplate_200ul', 6)
      plate384 = protocol.load_labware('corning3575_384well_alt', 5)
      p300m = protocol.load_instrument('p300_multi_gen2', 'left',
                                     tip_racks=[tips300])

      #buffs
      global buffs, buffa, buffb, buffc, buffd
      buffa = "a"
      buffb = "b"
      buffc = "c"
      buffd = "d"
      buffs = [buffa, buffb, buffc, buffd]
      del buffs[num_buffs:]

      global start_96well
      start_96well = well_96start

  def protein_titration(buff, protocol):
      prot_col = (buffs.index(buff)*3)+start_96well
      buff_col = prot_col+1
      extra_buff_col = buff_col+1
      start_384well = 0
      if (buffs.index(buff) % 2) == 0:
          which_rows = 0
      else:
          which_rows = 1

      p300m.pick_up_tip()
      p300m.distribute(20, plate96.rows()[0][buff_col].bottom(1.75),
                       plate384.rows()[which_rows][start_384well+1:start_384well+12],
                       disposal_volume=0, new_tip='never')
      p300m.blow_out()
      p300m.distribute(20, plate96.rows()[0][extra_buff_col].bottom(1.75),
                       plate384.rows()[which_rows][start_384well+12:start_384well+24],
                       disposal_volume=0, new_tip='never')
      p300m.blow_out()
      p300m.flow_rate.aspirate = 40
      p300m.flow_rate.dispense = 40
      p300m.transfer(40, plate96.rows()[0][prot_col].bottom(1.75),
                     plate384.rows()[which_rows][start_384well], new_tip='never')
      p300m.transfer(20,
                     plate384.rows()[which_rows][start_384well:start_384well+22],
                     plate384.rows()[which_rows][start_384well+1:start_384well+23],
                     mix_after=(3, 20), new_tip='never')
      p300m.blow_out()
      p300m.aspirate(20, plate384.rows()[which_rows][start_384well+22])
      p300m.drop_tip()