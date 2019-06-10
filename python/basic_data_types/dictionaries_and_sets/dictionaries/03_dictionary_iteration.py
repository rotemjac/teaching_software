

dictionary4 = dict(
    first_name = "Joe",
    last_name  = "Doe",
    phone      = 123456
)

#  Simplest way
print("--------------------------- Basic iteration --------------------- ")
for item in dictionary4:
  print(item)

print("--------------------------- Iteration with keys() --------------------- ")
#  This is like writing explicitly .keys()
for item in dictionary4.keys():
  print(item)

print("--------------------------- Iteration with values() --------------------- ")
#  Take values only
for item in dictionary4.values():
  print(item)

print("--------------------------- Iteration with items() --------------------- ")
# Iterate over both keys and values
for key, value in dictionary4.items():
  print(key, value)