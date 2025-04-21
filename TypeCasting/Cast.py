# This file is for learning type casting
# you can use str(), int(), bool(), float() to
# type cast
#
# author: CJ Quintero
# last updated: 04/21/2025

# fields
isPythonFile = True
price = 3.99
name = "Example User"
count = 5
emptyString = ""

# truncates 3.99 -> 3
print("Here is a float casted to an int: ")
print(int(price))

# turns 5 -> 5.0
print("Here is an int casted to a float: ")
print(float(count))

# concatenate strings
print("Here is price casted to a string: " + str(price))

# get type of price then convert it to a string to concat
print("Here is the type of <price>: " + str(type(price)))

# returns true
print("Here is a bool casted to a string: " + str(isPythonFile))

# returns false
# empty strings are FALSE if casted to a bool
# true if the string is not empty 
print("Here is an empty string casted to a bool: " + str(bool(emptyString)))