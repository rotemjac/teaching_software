
# --------------------------------- Definitions ------------------------------------ #

def multiply_small_numbers_only(num):

    if type(num) != int and type(num) != float:
        raise NotANumber

    elif num < 0 or num > 1000:
        raise NumberNotInRangeError

    else:
        return num *2

# --------------------------------- Custom Exceptions Definitions ------------------------------------ #

class NotANumber(Exception):
    def __init__(self):
        self.message = "The argument passed is not a number"

class NumberNotInRangeError(Exception):
    def __init__(self):
        self.message = "Please pass a number between 0 -1000"

# ------------------------------- Some tests -------------------------------------- #


input_num = 5
print("Test for int: " , multiply_small_numbers_only(input_num))

# Will raise the "NumberNotInRangeError" Exception
input_num = -5
print("Test for int out of range: " , multiply_small_numbers_only(input_num))

# Will raise the "NotANumber" Exception
input_num = "5"
print("Test for string: " , multiply_small_numbers_only(input_num))

