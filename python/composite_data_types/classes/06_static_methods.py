

# In the term "static" I mean - "Belong to the Class and not to the Object"
# Such a method, one that takes an instance (self) as the first parameter, is referred to as a bound method.

# The 'self' points to the current instance in the context - So instance methods must receive 'self' as the first argument

# But we can see that when calling instance methods, we don't pass it as an argument
# and there are no error. This is because Python pass the 'self' argument implicitly


# --------------------------------- Definitions ------------------------------------ #
class City:

    # This is a class level attribute which will be shared across all instances (and not be created PER instance)
    country = "USA"

    def __init__(self, name, location, population):
        self.name       = name
        self.location   = location
        self.population = population

    # We mark a static (class) method with the @classmethod attribute
    # All class methods must take a class argument as first param. The convention is to name is "cls" but class_ is also ok
    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

# ------------------------------- Some tests -------------------------------------- #

city1 = City("New York", "East", "12000000")
city2 = City("Los Angeles", "West", "10000000")

# Use the static method in the object
city2.change_country("Canada")

# Will be reflected in all objects
print("city1.country=",city1.country) # Prints Canada
print("city2.country=",city2.country) # Prints Canada
