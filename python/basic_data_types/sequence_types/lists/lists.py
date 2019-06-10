
some_list = ["11","22","33","44"]

# Indexing , Length and Slicing - Just like strings
print("Indexing example: " , some_list[2])
print("Length example: "   , len(some_list))
print("Slicing example: "  , some_list[2:4])

# Concatenation - You can concatenate 2 lists with the + operator
some_list2 = ["55","66","77", "88", "99"]
all_list = some_list+some_list2
print(all_list)

# Append
all_list.append("100")
print(all_list)


# List references
all_list2 = all_list
all_list2[5] = "000"
print("You will see that the 5th item in the first list also changed: " , all_list[5])
