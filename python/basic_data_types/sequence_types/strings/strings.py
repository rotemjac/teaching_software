

some_string = "This is a string"
some_string2 = 'This is also a string'

sentence = "I " + 'love ' + "Python"

print("Print just a few chars:", sentence[2] + sentence[3])

# Slicing
print("Print a slice:", sentence[2:6]) # Lest item not included

# Length
print("Length of sentence is: " , len(sentence))

# String Interpolation - From Python 3.6 - You need to add an "f" before the string
favorite_food = "apple"
print(f"My favorite food is {favorite_food} and I like it very much!")

print('-----------------------------------')

# multiple lines
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print(para_str)
