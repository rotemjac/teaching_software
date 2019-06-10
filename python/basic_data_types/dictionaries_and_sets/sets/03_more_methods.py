
# --------------------------------- Definitions ------------------------------------ #
set1 = {1,2,3,4,9,6,15}
set2 = {1,2,3,5,7,8,10,11}

# Union
print(" ---------------------- Union ------------------------- ")
print(set1.union(set2))

# Intersection
print(" ---------------------- Intersection ------------------------- ")
print(set1.intersection(set2))
print(set1 & set2) # Same as previous line

# Difference
print(" ---------------------- Difference ------------------------- ")
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

# Subsets
print(" ---------------------- Subsets ------------------------- ")
print(set1.issubset(set2)) # False

set3 = {1,2,3}
print(set3.issubset(set1))   # True
print(set1.issuperset(set3)) # True


# Equality
print(" ---------------------- Equality ------------------------- ")
print(set1 == set2) # False


#Some more built-in methods:

# difference_update()
# intersection_update()
# symmetric_difference_update()

# remove()
# clear()
# pop()
# discard()