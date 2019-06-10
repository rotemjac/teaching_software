
# Encapsulation is the concept of bundling data and methods that work on that data via a structure.
# In OOP languages (Pure OOP like Java, C# or non pure like Python) it will be a class
# In other languages it coul be other structure (in Golang it will be a struct)

# All the files in this directory are related to Encapsulation
# In this module will deal with the specific part in Encapsulation named information hiding

# In python - all attributes and methods are public (can be accessed from outside) by default.
# We can also make them:
#           private (only used in the specific class)    - with 2 underscores: "__"
#           protected (only used in the inherited class) - with 1 underscores: "_"

# This is not like most languages were you use the keywords of: public, protected and private

# --------------------------------- Definitions ------------------------------------ #
# A class with a private attribute "id"
class Person:
    def __init__(self):
        self.__id = 000

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

# ------------------------------- Some tests -------------------------------------- #

person1 = Person()

# Try to access a private attribute - we lead to AttributeError: 'Person' object has no attribute '__id'
# print(person1.__id)

# via the getter it will work
print(person1.get_id())

# Test the setter
person1.set_id(12345)
print(person1.get_id())

