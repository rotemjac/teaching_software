
# --------------------------------- Definitions ------------------------------------ #
def multiply_small_numbers_only(num):
    if type(num) != int and type(num) != float:
        raise Exception("Please pass a number")
    else:
        return num *2


# ------------------------------- Some tests -------------------------------------- #

input_num = 5
print("Test for int: " , multiply_small_numbers_only(input_num))

input_num = 5.6
print("Test for float: " , multiply_small_numbers_only(input_num))

input_num = "5.6"
print("Test for string: " , multiply_small_numbers_only(input_num))