In Python a module is any file with a .py extension. 
A Python module can contain any valid Python code you want and import it in other places of your project.

Modules
A module can also be a directory containing Python files. Adding an __init__.py file inside a directory will tell the Python interpreter that the indicated directory is a module and that it will be registered in Python's module namespace.
It is not a requirement anymore to add an __init__.py file, but it is a good practice to have one in case you need to run some custom code during module initialization.

Packages
A package is therefore defined as a collection of modules. Packages are a good way of separating your modules from other people's modules to avoid name clashes.

When you import a module, the code in the module will be executed exactly one time even if you have another place in the code importing the exact same module. 
Upon import, Python compiles the module's code, executes the code, and then populates the module's namespace with the resource names defined in the module. 
This makes the resources that have been imported accessible in the scope in which they have been imported.