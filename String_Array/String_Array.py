# Learning to use string arrays 
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0

# strings are 0 based, so the letter 'H' is text[0]
# and the '!' is text[27]
text = "Hello, I am learning Python!"

# prints the , in the string
print(text[5])

# prints the ! in the string
print(text[27])

# in python, the range can also be negative to print
# the chars in reverse

# printing this prints the last char of the string, so 
# in this case, ! is printed
print(text[-1])

# this is the 5th from last character, 't'
print(text[-5])

# string slicing

# note that the first value is always INCLUDED
# and the second value is always EXCLUDED

# prints chars 7 - 13
print(text[7:14])

# prints 7 to the end of the string
print(text[7:])

# prints beginning to 14
print(text[:14])

# get the string length

# python uses len(STRING_HERE) instead of str.len()
print("The length of the string is: " + str(len(text)))