In Python a module is any file with a .py extension. 
A Python module can contain any valid Python code you want and import it in other places of your project.

Modules
A module can also be a directory containing Python files. Adding an __init__.py file inside a directory will tell the Python interpreter that the indicated directory is a module and that it will be registered in Python's module namespace.
It is not a requirement anymore to add an __init__.py file, but it is a good practice to have one in case you need to run some custom code during module initialization.

Locating Modules
When you import a module, the Python interpreter searches for the module in the following sequences −

A. The current directory.

B. If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.

C. If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.

The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.


Packages
A package is therefore defined as a collection of modules. 
It is used to separate modules and avoid name clashes.

When you import a module, the code in the module will be executed exactly one time even if you have another place in the code importing the exact same module. 
Upon import, Python compiles the module's code, executes the code, and then populates the module's namespace with the resource names defined in the module. 
This makes the resources that have been imported accessible in the scope in which they have been imported.

Each package must contain a __init__.py file in the root of its directory.
This give the Python interpreter the indication that the directory is a module.
The file can be empty, but you can use it for some added functionality (for example, to specify exactly what can and cannot be imported from the package).
When you import a package, the code in the __init__.py file is executed by the Python interpreter to build the package and the package namespace.