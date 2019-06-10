

# Defining an empty class
class Animal:
    pass

# Instantiating 2 objects
anim1 = Animal()
anim2 = Animal()

# We can see hat the objects are NOT equal
isEqual = anim1 is anim2
print(isEqual)