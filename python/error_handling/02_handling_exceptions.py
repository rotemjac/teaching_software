
# --------------------------------- Definitions ------------------------------------ #


def multiply_small_numbers_only(num):
    if type(num) != int and type(num) != float:
        raise Exception("Please pass a number")
    elif num < 0 or num > 1000:
        raise Exception("Please pass a number between 0 -1000")
    else:
        return num *2


# ------------------------------- Some tests -------------------------------------- #

input_num = int(input("Please enter a number between 0 - 1000 \n"))

# Below is a common code for handling errors with exceptions handling

# 1. We first use the try block

# 2. If something goes wrong we catch the correct error with the correct Exception
#    in python we use the word 'except' for catching exceptions.

#    Notice that it is a bad practice to catch (except) all the error with the general "Exception"
#    we should write it at the end of all attempts, here I just added an attempt to catchValue Exception.

#    Notice that in order to catch the message from an inner exception,
#    we use the syntax "as X" where X can be e or err for example

# 3. At the end we can add a 'finally' keyword - the code in there will always run

try:
    res = multiply_small_numbers_only(input_num)
    print("Result is: " , res)

except ValueError:
    print("ValueError Exception occurred")

# The message added to the raised Exception will be inside err
except Exception as err:
    print("Some generic Exception occurred: " , err)

finally:
    print("This part will always run...")