# Conda environments

[Return to the Advanced Python - Conda, packages, and scripting mainpage](https://luger-lab.github.io/coding-tutorials/advanced_python_code/)

## [&larr; Back to contents](https://luger-lab.github.io/coding-tutorials/advanced_python_code/)

## What is Conda?
[Conda](https://docs.conda.io/projects/conda/en/latest/index.html) is a package management software that installs dependencies and manages environments in any coding language. Here, we will use it to manage Python environments. The reason we want to use it is that often certain software that we would like to run or develop requires certain packages and dependencies to run properly and can conflict with ones installed on our system. Because everyone's base system is configured differently we can use Conda environments to compartmentalize our Python environments to include only the packages we want and not affect the rest of our system. Many programs will install their own MiniConda or AnaConda managers to create and manage Python environments for specific software.

## Setting up a Conda environment
Let's try setting up a Conda environment. First, log onto our [sandbox](https://coding.csel.io/hub/login).

0. Now check to see if Conda is installed:
    ```
    jovyan@jupyter-shla9937:~$ which conda
    /opt/conda/bin/conda
    ```
    If it wasn't installed, we can learn how to install it [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

0. We can then create our first environment, where we specify what we want to call the environment and the version or Python or package we'd like to use:
    ```
    conda create --name new_env python=3.9
    ```
    Then, Conda will install all of the dependencies we've asked for inside this environment.

0. To see which environments we have access to we can use:
    ```
    jovyan@jupyter-shla9937:~$ conda env list
    # conda environments:
    #
    new_env                  /home/jovyan/.conda/envs/new_env
    swe4s                    /home/jovyan/.conda/envs/swe4s
    base                  *  /opt/conda
    ```
    Where the star denotes which environment we are currently in.

## Activating and deactivating environments
0. To activate our new environment we will use:
    ```
    conda activate new_env
    ```
    If that starts throwing errors:
    ```
    source /opt/conda/etc/profile.d/conda.sh
    ```
    You should now see the environment in front of your input bar:
    ```
    (new_env) jovyan@jupyter-shla9937:~$
    ```
    You are now in our new Conda environment.

0. To install new packages into our environment use:
    ```
    conda install package_name
    ```
    You can then see which packages are installed using:
    ```
    conda list
    ```
    And remove a package using:
    ```
    conda remove package_name
    ```
0. Once we are done with our package for the day we can "get out of it" by deactivating it.
    ```
    conda deactivate
    ```
## Removing environments
Because Conda environments can get pretty large you may want to remove old ones. You can do this by using the command:
```
conda env remove -n new_env
```

## [Continue to Python packages &rarr;](https://luger-lab.github.io/coding-tutorials/advanced_python_code/python_packages/)
