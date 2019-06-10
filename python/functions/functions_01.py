
def someFunc1(num):
    return num + 100


def someFunc2(num):
    return num + 200


some_num_str = input("Enter a number: ")
some_num_as_int = int(some_num_str) # Without the cast we'll get: "TypeError: must be str, not int"

print("Output of someFunc1: " , someFunc1(some_num_as_int) )
print("Output of someFunc2: " , someFunc2(some_num_as_int) )

print(__name__)