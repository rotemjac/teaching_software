

set2 = set([1,2,3,4,5])
print("set2: " , set2) # Prints: {1, 2, 3, 4, 5}

# ------------------------------ Add ------------------------------ #
set2.add(6)
print("set2: " , set2) # Prints: {1, 2, 3, 4, 5, 6}

# Add - another option - with update
# set2.update(7)   # Will cause a TypeError: 'int' object is not iterable
set2.update([7]) # Will work
print("set2: " , set2) # Prints: {1, 2, 3, 4, 5, 6, 7}

# ------------------------------ Read ------------------------------ #
print("--------------------- Read -----------------------")
for num in set2:
    print(num)
