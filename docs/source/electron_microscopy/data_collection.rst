Data collection
==================================
Negative stain
--------------
*adapted from Johannes Rudolph*

Goal
~~~~
Use the FEI Tecnai T12 TEM to image negative stain.


Getting started
~~~~~~~~~~~~~~~
#. Get trained by Garry Morgan (garry.morgan@colorado.edu)
#. Reserve time using the `online portal <https://www.colorado.edu/facility/ems/>`_
#. Log into the Windows server
#. Check liquid nitrogen dewar and top off if necessary on right hand side of column
#. Check if ``High Tension`` and ``Filament`` are on (buttons are yellow when on)

  - if not, turn them on (``High Tension`` first, then ``Filament``)
  - wait at least 5 min after turning on the filament to collect data
#. Gun/Col vacuum should ideally read log 6

  - if sample has been inserted, often goes to log 12-14
  - if higher than that, seek Garry's help
#. Make sure the column valves are closed (button should be yellow)
#. Make sure the beam is spread

  - open the viewing window and adjust using intensity dial
  -	if column valves are closed, you won't see anything
  - just set the C2 value on screen ~50%

Removing the sample holder
~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Pull straight out, resisting vacuum, with other hand on plate
#. Turn CW until it stops
#. Re-grip and break seal of vacuum with thumb on plate
#. Pull straight out the rest of the way, slowly

Loading grid into holder
~~~~~~~~~~~~~~~~~~~~~~~~
*Never touch bronze part of holder*

#. Use pin to 'open door'
#. Use tweezers to place grid into hole (can tap opposite end to position grid)
#. Use pin to 'close door'
#. Give a gentle shake to make sure grid stays in there

Inserting sample holder
~~~~~~~~~~~~~~~~~~~~~~~
#. Put pin at 2 o'clock (sample will be oriented vertically)
#. Insert slowly until pin hits a stop
#. Gently push holder while turning CW, another 1 -2 cm
#. Seal is created and red light/vacuum pump will go on (takes 1 min)
#. Then rotate CCW to stop
#. Vacuum will draw the holder in: guide it slowly so it doesn't go too fast

Setting up acquisition software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Open camera software (AMT icon) and move to other screen
#. Start a new case study under ``File>New Case Study``

  - Make a new folder under your lab and user on the ``192...`` server
  - Make a new case study with the sample and grid number (make a new one for every grid)

Eucentric focusing (alpha wobbler adjustment)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Open the column valves to let beam through the screen
#. Adjust mag and beam intensity and center on a feature of the grid
#. Press ``L1`` on left control panel to start alpha wobbler
#. Adjust Z-height on right control panel using light taps on plus/minus buttons until the feature no longer moves away from the center
#. Press ``L1`` again to turn off alpha wobbler
#. Press ``Eucentric Focus`` on right panel

Adjusting the beam
~~~~~~~~~~~~~~
#. Insert objective using lever on side of scope
#. Once in an area of interest, adjust mag and center beam with left track ball
#. Also adjust intensity with dial on left control panel (should be 4-5 nanoAmps)

Using the camera
~~~~~~~~~~~~~~~~
#. Press ``Insert Camera`` on top right of acquisition panel
#. Click ``Live Image``
#. Adjust beam intensity, focus and mag as needed (generally need a mag of >40K to see particles)
#. Click for final image and then right click on ``Save`` (this will close the final image and re-activate the live camera)

*Pro-tip: focus/mag/ adjust in one spot; then move to a new spot nearby for an "undamaged" image*

Adjusting FFT (as needed) - click on ``xxx``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _changing_grids:

Changing grids
~~~~~~~~~~~~~~
#. Click camera in to move the camera back out of the beam
#. Lower Mag to ~1000x
#. Reduce beam intensity to ~50%
#. Under ``Search`` tab of microscope control panel, click ``XY`` to reset stage
#. Close column valves **the most important thing!**

Leaving the microscope
~~~~~~~~~~~~~~~~~~~~~~
#. Do :ref:`changing_grids` protocol
#. Remove the holder from the microscope
#. Remove your sample from the holder
#. Re-insert the empty sample holder
#. If no one is signed up to use the microscope within an hour, turn ``Filament`` off.
#. Leave ``High Tension`` on and column valves closed
#. Log your time on the e-logger and the paper log
#. Transfer your images from the Windows server to Google Drive
