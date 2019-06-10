
# Syntax is very similar to lists but we use () instead of []


some_tuple = (11.5,"22",33,"Hello")

# Indexing , Length and Slicing - Just like strings
print("Indexing example: " , some_tuple[2])
print("Length example: "   , len(some_tuple))
print("Slicing example: "  , some_tuple[2:4])

# Concatenation - You can concatenate 2 lists with the + operator
some_tuple2 = ("55","66","77", "88", "99")
all_tuples = some_tuple+some_tuple2
print(all_tuples)

# -------------- Because of immutability - you can't use some methods in tuples ----------------- #

# Append
# AttributeError: 'tuple' object has no attribute 'append'
# all_tuples.append("100")
# print(all_tuples)


# List references
all_tuples2 = all_tuples

# TypeError: 'tuple' object does not support item assignment
# all_tuples2[5] = "000"
