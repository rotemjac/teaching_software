from pkg1 import *
print(dir()) # module_B will not be specified
# prints: ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'module_A', 'module_C', 'module_D']

from pkg2 import *
print(dir()) # module_F and module_H will not be specified
# prints: ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'module_A', 'module_C', 'module_D', 'module_E', 'module_G']

# Use the functionality exposed by the exposed modules
module_A.printer()
module_G.printer()