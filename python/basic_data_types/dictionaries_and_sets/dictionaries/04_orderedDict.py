

# The OrderedDict class is a dict subclass defined in the python's collections package.
# We'll use ordered dictionaries When it is important to store and retrieve data in a predictable order
# For example when working with database entries.

# OrderedDict are normal dictionaries which maintain the insertion order of keys.
# so in iteration you access the keys in the order in which they were inserted.


from collections import OrderedDict
ordr_dict = OrderedDict(name = "John", family="Doe", address="Some street")
print(ordr_dict)

print("------------------------------------------")

# You can see that OrderedDict contains some attributes that normal dictionary doesn't
print(dir(ordr_dict))
