


# Lets take a simple dictionary
dictionary4 = dict(
    first_name = "Joe",
    last_name  = "Doe"
)

print("--------------------------- Adding data --------------------- ")
# First way
dictionary4['phone'] = 123456
# Another way
dictionary4.update({'phone2': 789101112})


print("--------------------------- Reading data --------------------- ")
# Reading data - first way
print(dictionary4['phone'] )
# print(dictionary4['phoneXXX'] ) # Will throw a KeyError: 'phoneXXX'

# Reading data - better way
print(dictionary4.get('phone'))
print(dictionary4.get('phoneXXX')) # Display None
print(dictionary4.get('phoneXXX', 'Will display this message instead of None'))

print("--------------------------- Editing data --------------------- ")
# First way
dictionary4['phone'] = 111222
# Another way
dictionary4.update({'phone2': 5555})

print(dictionary4.get('phone'))
print(dictionary4.get('phone2'))


