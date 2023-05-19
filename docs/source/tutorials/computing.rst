Basic computing - Linux, Bash, and SLURM
========================================

Goal
----
To give a basic introduction to coding (in Bash) and how to use Linux based machines.

    - :ref:`linux`
    - :ref:`bash`
    - :ref:`navigation`
    - :ref:`variables`
    - :ref:`arrays`
    - :ref:`loops`
    - :ref:`if`
    - :ref:`while`
    - :ref:`text editors`
    - :ref:`running`
    - :ref:`connecting`
    - :ref:`advanced`
    - :ref:`slurm`
    - :ref:`practice`

.. _linux:

Linux
-----
Linux is the kernel on which most high performance computing (HPC) is done. A kernel is the software that allows an operating system to control physical hardware. The Linux kernel is based on UNIX and is open source and free to use by anyone, as its creator `Linus Tuvolds <https://en.wikipedia.org/wiki/Linus_Torvalds>`_ started the kernel under a GNU license back in the early 90's. Anyone can contribute code to the kernel, as long as it passes a series of revisions and oversight. Because so many people contribute to the code it is constantly being improved.

To use Linux, you need a distribution (shortened to 'distros'). These distros are tantamount to operating systems (think Windows or MacOS). There are many to choose from: free ones like Ubuntu or Tux and enterprise ones like RedHat and CentOS. Whichever distro you choose, they will all act the same under the hood, even if the desktop appearance is different, because they all operate using the same kernel.

Although many Linux applications have easy to use graphical user interfaces (GUIs), a savvy Linux user will learn how to do everything within a terminal. A terminal is an access point into a computer that takes and returns text commands. Computing through a terminal is almost always faster than using a GUI and generally offers the user more options and customization than a GUI. The language Linux-based operating systems use in the terminal is called Bash.

.. _bash:

Bash
----
#. Description
    Bash is a powerful programming language that Linux-based operating systems use to perform tasks. Most of the time user-facing programs will use an easier language to debug like Python or MatLab, but you will need to use Bash to navigate around the terminal and launch jobs.

#. Setting up a sandbox
    A sandbox is a safe environment in which to code without being able to break your computer. In our case we will be using CU's Computer Science coding space :

    https://coding.csel.io/hub/login

    - All you need to do is sign in with your CU credentials.
    - Once logged in click on the 'Default Coding Environment' widget (we'll discuss how this service actually works in a later tutorial).
    - You can bookmark this site for later use.
    - In this code space, you'll see a file tree on the left side and a series of widgets on the right, we'll discuss how to use a few of these over the course of this series.
    - For now, click on the black 'Terminal' widget in the bottom row. What you've opened is a Linux terminal emulator that we will use to learn basic Bash commands.

#. Basic commands
    Commands in bash are entered directly into the command line, generally in the following format:

    .. code-block:: bash

      <command> --<option> <input>

    The command is executed when you press enter.

    - The commands are actually executable scripts somewhere in your PATH (usually in your bin folder).
    - Options or "flags" modify the command in someway, like changing the behavior or explicitly defining some input/output. Most of the time, the long form of the option will have two dashes, as in:

    .. code-block:: bash
      
      ls --all

    Whereas one letter abbreviations use one dash:
    
    .. code-block:: bash

      ls -a

    - Inputs are generally file names or a value required by the option defined.
    - As a rule of thumb, most programs will return a brief documentation page when ran with the flag ``--help``:

    .. code-block:: bash

      ls --help

    #. ``ls`` This first command, 'ls' lists the files and directories in your current folder or 'directory' as it's called in Linux. Two common flags to use with ls are '-a' and '-l'.
        
        .. code-block:: bash
    
          jovyan@jupyter-shla9937:~$ ls
          cs_class
     
        - ``ls -a`` returns 'all' the files and directories in a give directory, including hidden ones, whose names start with a '.', we'll talk about these in a later tutorial.
            
            .. code-block:: bash

              jovyan@jupyter-shla9937:~$ ls -a
              .   .bash_history            .bashrc  .conda    .config   .empty      .ipynb_checkpoints  .jupyter  .python_history
              ..  .bash_history-00035.tmp  .cache   .condarc  cs_class  .gitconfig  .ipython            .local    .wget-hsts

        - ``ls -l`` will return the 'long' version of a file name, including permissions, owner, size, and date created.
        
            .. code-block:: bash
              jovyan@jupyter-shla9937:~$ ls -l
              total 4
              drwxr-sr-x 11 jovyan users 4096 Aug 26 17:49 cs_class
            
    #. ``pwd`` The next thing we need to know is where we are, we can figure this out by using the command `pwd`, which prints the working directory and will give an output like:
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ pwd
          /home/jovyan
        
        Here, each backslash represents another layer of the file tree and is know as the 'absolute path'. Try it and see where you are, as we move about later, try it again to keep oriented.

    #. ``echo`` If you simply want to return some text or the value of a variable, you can use ``echo <word, phrase or variable>``. Try to return the phrase 'Hello world'.
        
        .. code-block:: bash
        
          jovyan@jupyter-shla9937:~$ echo Hello world.
          Hello world.
        
    #. ``touch`` There are many ways to make a new file, but the most direct way is simply ``touch <filename>``. This command creates an empty file that you can then do things with. Try this command using your own filename and use the extension '.txt' **remember not to ``touch`` a filename that already exists as it will overwrite it.**
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ touch dummy.txt
          jovyan@jupyter-shla9937:~$
        
    #. ``mkdir`` Similar to touch, we can also make a directory using `mkdir <directory_name>`.
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ mkdir new_directory
          jovyan@jupyter-shla9937:~$
        
    #. ``cp`` One thing you can do with this new file is 'copy' it. This is the first command we've used that requires two arguments: ``cp <source_file> <destination_file>``
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ cp dummy.txt copy_of_dummy.txt
          jovyan@jupyter-shla9937:~$
        
        - In Bash, spaces separate arguments, therefore don't use them in filenames. If you need to specify a filename with a space in it, you will need to wrap it with quotes. Anything inside a set of quotes is treated as a single argument: ``'file name with space.txt'``. Use underscores if you need to separate words: ``file_name_without_spaces.txt`` Try to copy the file you made, remember to use a new name, otherwise you'll overwrite it.
        - We can also copy the directory we made by using ``cp -r <directory_name> <new_name>``. The '-r' here stands for 'recursively' or 'go through and copy everything in this directory'.

    #. ``rm`` Now that we have two files that are copies of each other, we can delete the original. To do this we'll use the ``rm`` or 'remove' command, here we need only specify the file to remove:
        
        - ``rm <filename>`` Try it.
        - Now try to remove the copied directory we just made. Bash is smart like this and doesn't want us to remove a directory on accident. To remove an entire directory we will have to do it recursively: ``rm -r <directory_name>``
    
    #. ``>`` To 'direct' the output of a function into a file, we can use ``<some_function> > <filename>``. **Be careful, as this function will overwrite whatever is in a file.** Try using the ``echo`` function to write a phrase into a .txt file.
    #. ``cat`` To figure out if we successful in writing to the file, we can use ``cat <filename>``. It is a quick way to read all the contents of file. The caveat here is that it will read ALL the contents, no matter how long.
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ cat dummy.txt
          This is a file called dummy.
        
    #. ``head`` This is where ``head -n <#> <filename>`` comes in handy. It will only read the first number of lines specified with '-n' (if you don't use the n flag, it will read 20 lines).
        
        .. code-block:: bash

          jovyan@jupyter-shla9937:~$ head -n 4 dummy.txt
          This is a file called dummy.
          line2
          line3
          line4
        
    #. ``tail`` Tail is the opposite of head; it reads the last number of lines you specify ``tail -n <#> <filename>``.
    #. ``>>`` If you'd like to add something to the end of file you can use the double carrot ``echo <phrase> >> <filename>``
    #. ``|`` Finally, to put multiple functions together, use the ``|``. This function takes the output from the previous function and inputs it into the next one. This is called piping. Try something like ``mkdir <directory_name> | cd <directory_name> | touch <new_file | echo <phrase> > <new_file> | cat <new_file> ``.

.. _navigation:

Navigation
----------
#. ``cd`` To navigate from directory to directory, we can use ``cd`` or 'change directory'.
    
    - We can move into a deeper directory by ``cd <directory name>``
    - Up a directory with ``cd ..`` ('..' represents the parent directory)
    - The same directory ``cd .`` ('.' represents your current directory, we'll use it later)
    - An adjacent directory by specifying a 'relative path' ``cd ../jon``
    - A specific directory by specifying the absolute path ``cd /home/jon``
    - Your home directory with either ``cd ~`` or simply ``cd``

#. ``mv`` Similar to, and much faster than the ``cp`` function, we can use ``mv <source_file> <destination_file>`` to move a file from one location to another. Because you are not actually copying and remove the file, simply changing its location information, this function is often instant. Another use of this function is to rename files (because that is essentially what you are doing). To do this simply ``mv <old_name> <new_name>``, you can also move and rename entire directories.
#. ``Tab filling`` One of the biggest timesavers in coding is using the tab key to autofill a function in your path or the name of a file/directory after you have typed the first few characters. Tabbing twice will give you a list of all files or directories in your current directory.
#. ``Permissions`` All files and folders on a computer have a set of permissions, which you can view using ``ls -l``. There are three levels of permissions: user, group, and other. And three types of permission in each level: read(r), write(w) and execute(x). These are denoted by sets of 3 letters per level.
    
    .. code-block:: bash

        -rwx------ 1 shla9937 lugerlab 0 Sep  3 16:48 user.txt
        -rwxrwxr-- 1 shla9937 lugerlab 0 Sep  3 16:48 group.txt
        -rwxrwxrwx 1 shla9937 lugerlab 0 Sep  3 16:48 other.txt
        
.. _variables:

Variables
---------   
- Variables can be defined in bash using the syntax: ``<varibale_name>=<variable_value>``
- You can then call the variable using ``$<variable_name>``
- And clear its value with ``unset <variable_name>``
- Try setting up a variable and calling its value with the ``echo`` command.

.. _arrays:

Arrays
------
Lists in many programming languages are called 'arrays' in Bash. Simply put and array is an ordered list of values (numbers, strings, ect.) that you can iterate through.

#. Make an empty array ``<array_name> = ()``
#. Make a filled array ``<array_name> = (<value0> <value1> <value2>)``
#. Return first value ``${<array_name>}`` (use echo to print the output)
#. Return specific value ``${<array_name>[i]}`` where i is the index (or position) of the value in the list, remember arrays start indexing at 0.
#. Return all values ``${<array_name>[@]}``
    
    .. code-block:: bash

        jovyan@jupyter-shla9937:~$ echo ${array1[@]}
        0 1 2 3 4 5
    
#. Return array size ``${#<array_name>[@]}``
#. Change value of first element ``<array_name>[0]=<new_value>``
#. Append value to list ``<array_name>+=(<value>)``

.. _loops:

For Loops
---------
Now that you can use variables and arrays, you can use loops to iterate through those arrays and perform functions.

A 'for loop' will iterate through all the elements of an array and perform the same function, as in 'for each element, do this' and that is actually how the syntax works in bash.

    - First, declare the for loop, variable to be iterated, and iterable element through which to iterate and add ``; do``:
        
        .. code-block:: bash

            for i in ${array1[@]}; do
        
    - Next, tell the loop what to do with each iteration:
        
        .. code-block:: bash
            > echo ${array1[i]}
        
    - You can add another function or declare the end of the loop and tell Bash to execute it:
        
        .. code-block:: bash
            > done
        
    - Here's an example of a for loop that looks at all the elements in an array and prints one each round:
        
        .. code-block:: bash
            jovyan@jupyter-shla9937:~$ for i in ${array1[@]}; do
            > echo ${array1[i]}
            > done
            0
            1
            2
            3
            4
            5
        

.. _if:

If statements
-------------
If statements are a powerful tool that allow you to execute commands only if a specific condition has been met. There are three possible conditions in an if statement:
    
    - ``if`` runs a command if the condition is satisfied.
    - ``else`` runs a command if none of the previous conditions are met.
    - ``elif`` runs a command if the previous if's conditions are unsatisfied and the condition set forth by the elif is satisfied.
    - the basic syntax for an if statement in bash is:
        
        .. code-block:: bash

          if [ <condition> ]
          then
              <command>
          elif
              <elif_command>
          else
              <else_command>
          fi
        
    - the ``fi`` denotes the end of the statement (it is simply if backwards)
    - if statements are often placed inside loops and can trigger them to end at certain times.
    
.. _while:

While loops
-----------
A while loop runs a command over and over until some condition is not met. It's kind of like putting an if statement inside of for loop that ends when a condition becomes false.
   
    - The basic syntax is:

        .. code-block:: bash
          
          while [ <condition> ]
          do
              [ <command> ]
          done
        
    - One caveat with while loops is that if the variable in the condition never changes or will never become false, you'll start an endless while loop. For loops generally iterate through a iterable object of a define size and so usually don't get caught in this behavior.

.. _text editors:

Text editors
------------

#. ``Nano`` Nano is one of the simplest command line text editors you can use and is installed on almost all Linux machines. It is great for quick edits, but is hard to debug unless you are intimately familiar with your script.
    
    - ``nano <new_file>`` will create a file and open it in the edit (a common behavior with most editors)
    - move around with arrow keys
    - ``ctrl+x``` exits the program, but asks if you want to save your file as the same name or a different one. Answer `y` to save and exit or `n` to exit without saving.
    - see more: https://www.nano-editor.org/docs.php

#. ``Vim`` Vim is one of the most widespread command line text editors because it color codes text and helps the use more than nano. Vim suffers from terrible documentation although you can always google your question to figure it out.
   
    - ``vi <new_file>`` creates and opens a file
    - Vim has two modes: edit and command. When in edit mode, you can make changes to your document.
    - ``esc`` gets you from the edit mode to command input mode (you can't exit until you get to command mode).
    - ``:q`` quits the editor without saving
    - ``:qw`` quits and writes (saves) the file
    - some documentation: https://www.vim.org/

#. ``Gedit`` Gedit is a graphical editor that may not come installed on your Linux machine, but many find easy to use.
  
    - ``gedit <new_file>`` creates and opens a gui with your file to edit it.
    - Documentation: https://help.gnome.org/users/gedit/stable/

#. ``Atom`` A really powerful graphical text editor that I like to use is called Atom and is built by Github, specifically to work well with Github. You can downloaded it and find out more at https://atom.io/
#. ``VScode`` Is another really good GUI editor made my Microsoft

.. _running:

Running scripts
---------------

Now that we know how to use bash and edit files, we can make scripts. Scripts are files that contain a series of commands that we can run, use to streamline pipelines, and share with others.
   
    - ``<program_name> <script_name>`` is the general formula for running scripts.
    - ``bash <script.sh>`` is how we can run a script using bash. The file extension ``.sh`` is often used to specify a bash specific script.
    - Eventually, we will learn how to input values into the script and how to make them executable.

.. _connecting:

Connecting to remote computers
------------------------------

#. ``ssh`` To log into a terminal securely from one Linux (or Mac) machine to another you can open a terminal and use ``ssh <user>@<computer_address>``. To stop the connection use ``exit``.
#. ``PuTTY`` `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ allows Windows machines to ssh into Linux machines using a GUI to produce a terminal emulator on the Windows end.

.. _advanced:

Advanced commands
-----------------

#. ``top`` Checks jobs running in the local environment.
#. ``crtl+c`` Kills the currently running job in a terminal. Can be dangerous as it simply interrupts.
#. ``history`` Displays inputs to your command line back a certain amount of time. Useful for remembering how tou did something you forgot to write down or put in a script.
#. ``clear`` Clears out all of the displayed command line (not your history).
#. ``*`` This is the symbol for a 'wildcard' it will do your command on everything matching your pattern. ``cat *.txt`` will read all text files in your directory. ``mv red* new_red_folder`` will move anything starting with 'red' into the 'new_red_folder'.
#. ``rsync`` A smart ``scp``. Use ``rsyn -auP source_directory destination_directory`` to make a copy of a folder. Running this command a second time will update and existing files and copy new ones. This makes keeping a copy of a file super simple becuase you don't have to copy every single file each time, just ones that have changed.
#. ``grep`` Use ``grep "<keyword>"`` to find a matching pattern in a list of files or ``grep "<keyword>" <file_name>`` to look inside of a file and find a keyword.
#. ``screen`` A powerful tool for keeping a terminal alive and returning to it later.
      
        - ``screen -S <screen_name>`` creates a screen_name
        - ``ctrl+a+d`` detaches the screen and allows it to run even if you logout or disconnect your computer (not if it gets turned off).
        - ``screen -r <screen_name>`` reatches the screen session.
        - ``exit`` from inside the screen will kill the screen session.

#. ``sudo`` 'Super User Do' can be placed in front of commands that require superuser privileges. You usually don't have the ability to use this unless it's on your own computer. **If you google something and it tells you to use sudo to fix it, don't. Sudo commands can irreversibly mess up your computer.**  

.. _slurm:

Slurm
-----
`SLURM <https://slurm.schedmd.com/overview.html>`_ is a workload manager common to most HPC clusters that allows users to submit jobs to it and then allocates resources based on a number of parameters. We will use this to do work on the `BioKEM <https://cu-biokem.github.io/BioKEM_docs/>`_ cluster. There many advantages to running jobs on clusters including access to orders of magnitude more resources, reproducible environments, and the ability to maximize computing efficiency.

#. Sbatch scripts - the scripts SLURM requires. They start with a header which contains information that SLURM will use to allocate resources and run the script. There are four main parts of an Sbatch script:
     
      - Specification of which language to interpret the script. This section is denoted by a shebang followed by the path to the binary, in most cases: ``#!/bin/bash``
      - Next are all of the SLURM parameters. Which ones are required are cluster specific, but generally you should be as explicit as possible, we'll talk more about these parameters in a later tutorial.
      - Then, you'll load all of the modules you need to run your program ``module load <modules>``.
      - Finally, you can run your commands.
      - You can use the .sbatch file extension to denote files
          
          .. code-block:: bash

            #!/bin/bash
            #SBATCH -p <partition> # Partition or queue.
            #SBATCH --job-name=<job_name> # Job name
            #SBATCH --mail-type=END # Mail events (NONE, BEGIN, END, FAIL, ALL)
            #SBATCH --mail-user=<email@colorado.edu>
            #SBATCH --nodes=<#> # Only use a single node
            #SBATCH --cpus-per-task=50 # cpus
            #SBATCH --mem=24gb # Memory limit
            #SBATCH --time=24:00:00 # Time limit hrs:min:sec
            #SBATCH --output=/Users/%u/slurmfiles_out/slurm_%j.out # Standard output and error log
            #SBATCH --error=/Users/%u/slurmfiles_err/slurm_%j.err # %j inserts job number

            module load <modules>
            <commands>

#. Queues - When you submit a job to SLURM, it goes into a queue where it wait to run.
      
    - Running the command ``squeue`` shows you what is going on in the cluster's queue:
        
        .. code-block:: bash

        fiji-1:~$ squeue
        JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
        7861375      long    job_0 ding1018  R 7-13:11:09      1 fijinode-60
        7874945     titan nf-dreg_ lysa8537 PD       0:00      1 (Resources)
        7874946     titan nf-dreg_ lysa8537 PD       0:00      1 (Priority)
        
    - You get cursory information about everyone's jobs on the cluster and see where it's running (node name), if it's at the top of the queue waiting for resources to open up (Resources), or if it's lower in the queue waiting for other jobs to run (Priority)

#. Out and error files - Running an Sbatch job will make two files with the jobid followed by the extensions .out or .err. You will need to you specify the folders you want these deposited into in your Sbtach header. The .out (output) file will give you any outputs that would normally appear on the command line during the run. The .err (error) file is useful for debugging and understanding what went wrong during failed runs.
#. Starting, stopping, and monitoring jobs

    - To start a single Sbatch job use ``sbatch <script_name.script`` this will give you a jobid that you can use to monitor your job status.
    - To stop a job that you no longer want to run or is failing in someway use ``scancel <jobid>``. You can only cancel your own jobs.
    - To check the status of all the jobs in a queue use ``squeue`` if you only want to see your jobs ``squeue -u <your_user>``

.. _practice

Practice
--------

#. Use a text editor to make and run a bash script that produces a text file containing a message.
#. Use a text editor to make and run a bash script that uses a loop to append a message 20 times times onto the previous text file.
#. Use a text editor to make and run a bash script that creates an array of file names, then uses a for loop to create all of the files.
