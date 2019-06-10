
# Option 1
# This does not make the module contents directly accessible to the caller (current module)
# The objects that are defined in the module remain in the module’s private symbol table
# objects in the module are only accessible when prefixed with <module_name> via dot notation, as illustrated below
import module_1
module_1.printer()


# Option 2 - import specific resource
from module_2 import printer
printer()

# Option 3 - import specific resource and give alias
from module_3 import printer as my_printer
my_printer()

# Option 4 - Not recommended to import ALL
from module_4 import *
printer()