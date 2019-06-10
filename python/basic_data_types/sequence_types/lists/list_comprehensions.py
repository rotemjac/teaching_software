

# List Comprehensions
# A very nice feature in python - a common use case is when we need
# to create a list that each element is the result of some operations applied
# to each member of another sequence or iterable object.


numbers = [1, 2, 3, 4, 5]
power_of_numbers = [num * num for num in numbers]
print(power_of_numbers)

# You can also use an "if" statement inside
power_of_numbers_except__power_of_4 = [num * num for num in numbers if num != 4]
print(power_of_numbers_except__power_of_4)
