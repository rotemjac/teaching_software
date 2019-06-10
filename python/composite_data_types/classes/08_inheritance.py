

# --------------------------------- Definitions 1 ------------------------------------ #

# Python syntax for inheritance
# Instead of writing "Subclass Extends Superclass" we write "Subclass(Superclass)"
class Superclass:
   pass

class Subclass(Superclass):
   pass

# --------------------------------- Definitions 2 ------------------------------------ #

# The super() method is used in order to access inherited methods
# from a parent class that has been overwritten in the child class.

class Animal:

   def __init__(self, age):
       self.age = age

class Dog(Animal):
   def __init__(self, age , name):
       super().__init__(age)
       self.name = name

# ------------------------------- Some tests 2 -------------------------------------- #
dog1 = Dog(7, "snoopy")

# age attribute is inherited from the Animal class
print("dog1.age: "  , dog1.age)

# name attribute is unique to the Dog class
print("dog1.name: " , dog1.name)
