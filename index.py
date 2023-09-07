# print("Hello World!")

# This is a comment
# if 5 > 2:
#     print("Five is greater than two")

"""
This is a comment
with multiple lines
"""

# Variable does not need to declare its data type and changeable
# q = 5
# q = "Aqilah"
# print(q)

# CASTING - specify data type, 'type()' - get the data type
# x = str(3)      # "3"
# y = int(3)      # 3
# z = float(3)    # 3.0
# print(x)
# print(y)
# print(z)
# print("\n")
# print(type(x))
# print(type(y))
# print(type(z))
# print(x, y, z) - output variables with same or different data type
# print(x + y + z) - output combined string variables or added numerical variable

# COLLECTION
# fruits = ["Apple", "Orange", "Banana"]
# x, y, z = fruits    # unpack collection
# x = y = z = fruits  # assign same value to multiple variables
# print(x)
# print(y)
# print(z)
# print(fruits)

# GLOBAL VARIABLE
# x = "awesome"
# def myFunc():
#     print("Python is " + x)
# myFunc()

# LOCAL VARIABLE
# x = "awesome"
# def myFunc():
#     x = "fantastic"
#     print("Python is " + x)
# myFunc()
# print("Python is " + x)

# global KEYWORD
# - create global variable inside function and make the variable belong to global scope
# def myFunc():
#     global x
#     x = "fantastic"
# myFunc()
# print("Python is " + x)
# - change global variable value inside a function
# x = "awesome"
# def myFunc():
#     global x
#     x = "fantastic"
# myFunc()
# print("Python is " + x)

# STRINGS
# Multiline strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
# """
# print(a)
# - is an array of bytes representing unicode characters
# txt = ' The best things in life are free!'
# print("free" in txt)
# print('free' not in txt)
# print(txt[2:5])     # start from position 2 and stop at position 5 (character in position 5 is not included)
# print(txt[:5])      # from start and stop at position 5 (character in position 5 is not included)
# print(txt[2:])      # start from position 2 until end
# print(txt[-5:-2])   # (from the end, not index) slice from position 5 until position 2 (character in position 2 is not included)
# print(txt.upper())              # upper case
# print(txt.lower())              # lower case
# print(txt.strip())              # remove whitespace in the beginning
# print(txt.replace('h', 'J'))    # replace string with another string
# print(txt.split(' '))           # returns list of text between specified separator (ie: ' ')
# format() - take passed arguments, format into string and put in the string where placeholders {}
# age = 23
# weight = 58.6
# height = 168
# txt = "My name is Aqilah. I am {} years old. My height and weight are {} and {} respectively"
# txt = "My name is Aqilah. My height and weight are {2} and {1} respectively. I am {0} years old"    # indexes to place arguments correctly
# print(txt.format(age, height, weight))  # can take single or multiple arguments
txt = "We are the so-called \"Vikings\" from the north."    # put escape character (backslash with character) to print unallowed character
print(txt)