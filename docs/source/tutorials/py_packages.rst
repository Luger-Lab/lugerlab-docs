# Python packages

[Return to the Advanced Python - Conda, packages, and scripting mainpage](https://luger-lab.github.io/coding-tutorials/advanced_python_code/)

## [&larr; Back to Conda environments](https://luger-lab.github.io/coding-tutorials/advanced_python_code/conda_environments/)

## What is a package?
On the last page we worked with adding and removing Python packages from a Conda environment, but what is a Python package? Broadly speaking, a package is a group of Python scripts written to perform a task together. This might be a big graphing package like MatPlotLib or something simply like Time, which simply manages time. Because these packages are modular, they can be added as needed and updated individually (which can lead to problems).

## Installing a new package
Installing a package in your Conda environment was relatively straight forward. So too, is installing packages on your system in general. Most packages can be installed using a simple PIP install.
```
pip install new_package
```
You can also update packages with:
```
pip install --upgrade old_package
```

## Importing a package
Once installed you can use this package in a Python shell or script by importing it.
```
import package
```

## [Continue to Scripts &rarr;](https://luger-lab.github.io/coding-tutorials/advanced_python_code/scripts/)
