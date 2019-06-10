

# -------------- Basic syntax -------------- #

# Both ways are equivalent - In both cases, a dictionary object will be created.
dictionary1 = {}
dictionary2 = dict()


# -------------- Some more methods -------------- #
# The dir() function - used to inspect the attributes and properties defined on the dictionary object
print(dir(dictionary1))

# You can check if a a data structure is a dictionary like this
# (This is not a feature of dictionaries - you could replace the 'dict' keyword with other types: str, int, tuple list)
print(isinstance(dictionary1, dict))


#  More built-in methods of dictionaries:
#   update() - used for both adding and editing
#   clear()
#   pop()
#   del()
#   copy()
#   popitem()
#   setdefault()
#   fromkeys()