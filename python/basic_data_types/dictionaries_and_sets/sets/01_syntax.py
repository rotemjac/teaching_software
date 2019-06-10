

# 2 ways to define a Set

# 1 - With curly bracket notation

set1 = {'a','b', 'c', 'd'}
print("set1: " , set1) # Prints: {'c', 'b', 'a', 'd'}


# 2 - With The Set function
# takes either an iterable (like tuple, list)
# or a sequence (like tuple, list , strings).

set2 = set([1,2,3,4,5])
print("set2: " , set2) # Prints: {1, 2, 3, 4, 5}

set3 = set((1,2,2,3,3,4,4,5))
print("set3: " , set3) # Prints: {1, 2, 3, 4, 5}