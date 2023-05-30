Data analysis
=============

Your images may be delivered in a single MRC stack, if this is the case, 
you will need to convert it to single image MRCs using the ``Imod`` command 
(use SBGrid on a workstation or CURC):

    .. code-block:: bash

       newstack -split 1 -append mrc <mrc_input_file> <output_file_root>
