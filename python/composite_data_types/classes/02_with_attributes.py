
# This correct way to add attributes to an object is to define them in the object's constructor method
# In Python it is __init__()

class Center:
    def __init__(self, phone):
        self.phone = phone

# If you do not pass the phone argument you wil get: TypeError: __init__() missing 1 required positional argument: 'phone'
center1 = Center("123456")
print(center1.__dict__)  # shows all object attributes and the values

# ------------------------------------------------------------------------------------- #

# A possible way to add attributes - not recommended because its less readable
# Empty class
class Worker:
    pass

# Adding attributes inline
worker2 = Worker()
worker2.phone = "123456"
print(worker2.__dict__) # shows all object attributes and the values