

# -------------- Basic syntax -------------- #

# Both ways are equivalent - In both cases, a dictionary object will be created.
dictionary1 = {}
dictionary2 = dict()

# See the syntax differences between the two ways

# Here we wrap the key with "" and assign with :
dictionary3 = {
    "first_name" : "Joe",
    "last_name"  : "Doe"
}

# Here we Dont need to wrap the key with "" and assign with =
dictionary4 = dict(
    first_name = "Joe",
    last_name  = "Doe"
)