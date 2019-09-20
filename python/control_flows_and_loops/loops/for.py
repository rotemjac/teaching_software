list = [100, 200, 300, 400, 500]

# In python we use the "for..in" loop - An example for basic loop syntax
for item in list:
    print(item*2.5)
print("--------------------")

# You can add a "else" at the end
for item in list:
	print(item)
	last_item_printed = item
else:
	print('The last item was ', last_item_printed)

print("--------------------")

# Using break, continue, pass
for item in list:
	if item < 300:
		pass
		print(item," - Small item") # will print after pass
	elif item < 400:
		continue
		print("This will never be printed")  # will not print after continue
	else:
		print("item is 500")
		break