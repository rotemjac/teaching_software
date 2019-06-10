import random

# Give me a random number between 0 and 100
some_random_number = random.randint(0,100)
print(some_random_number)

# If example
if some_random_number < 50:
	print("Small")
else:
	print("Big")


# elif - else-if
if some_random_number < 50:
	print("Small")
elif some_random_number < 80:
	print("Medium")
else:
	print("Big")




