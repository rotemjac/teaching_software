
# Definition of the lambda function (left side the arguments, right side is the expression)
answer = lambda x, y : x * y

num_str1, num_str2 = input("Enter a two numbers: ").split()

# We have to cast or else we'll get: TypeError: can't multiply sequence by non-int of type 'str'
num1 = int(num_str1)
num2 = int(num_str2)
print(answer( num1, num2))
