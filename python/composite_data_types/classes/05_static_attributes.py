

# In the term "static" I mean - "Belong to the Class and not to the Object"

# All attributes that are declared in the constructor are instance attributes
# They are bound to the instance in the __init__ method, where attributes are added to self.

# --------------------------------- Definitions ------------------------------------ #
class City:

    # This is a class level attribute which will be shared across all instances (and not be created PER instance)
    country = "USA"

    def __init__(self, name, location, population):
        self.name       = name
        self.location   = location
        self.population = population

# ------------------------------- Some tests -------------------------------------- #

city1 = City("New York", "East", "12000000")
city2 = City("Los Angeles", "West", "10000000")


# Prints: {'name': 'New York', 'location': 'East', 'population': '12000000'}
# The 'country' attribute does not display
print(city1.__dict__)

# There won't be a "AttributeError" because the object city1 will access the country attribute which belongs to the class
print(city1.country) # Prints USA

# ----------------------------------------------------------------------------- #

print("------------------------------------------------------------------------")

# Lets change a class attribute from the class - will be reflected in all objects
City.country = "Mexico"
print("After changing a class attribute from the class - city1.country=",city1.country) # Prints Mexico
print("After changing a class attribute from the class - city2.country=",city2.country) # Prints Mexico

# ----------------------------------------------------------------------------- #
print("------------------------------------------------------------------------")

# First, lets return to previous state
City.country = "USA"

# Lets change a class attribute from the other instance
# This will create a new attribute 'country' on the city2 object and it will not refer to the
# country attribute in the class
city2.country = "Mexico"

print("After changing a class attribute from the city2 object - City.country="  , City.country)  # Prints USA
print("After changing a class attribute from the city2 object - city1.country=" , city1.country) # Prints USA
print("After changing a class attribute from the city2 object - city2.country=" , city2.country) # Prints Mexico
