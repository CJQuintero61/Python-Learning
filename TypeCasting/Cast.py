# This file is for learning type casting
# you can use str(), int(), bool(), float() to
# type cast
#
# author: CJ Quintero
# last updated: 04/20/2025

# fields
isPythonFile = True
price = 3.99
name = "Example User"
count = 5

# truncates 3.99 -> 3
print("Here is a float casted to an int: ")
print(int(price))

# turns 5 -> 5.0
print("Here is an int casted to a float: ")
print(float(count))

# concatenate strings
print("Here is price casted to a string: " + str(price))

# prints "<class 'bool'>" to the console
print(type(isPythonFile))

# you can also type cast to bool
# false if the string is empty, true otherwise

# prints true
print(bool(isPythonFile))

