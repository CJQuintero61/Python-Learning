# Learning to use variables and formatting the output
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0

# defining variables in python does not require
# data types
length = 4.35
width = 1.89
name = "CJ Quintero"
nameCopy = 'CJ Quintero'
isStudent = True # bools must be capital 
isGraduated = False


# use print(f"...{variable}") to format the output
# no space is allowed between print(f"...")
print(f"The length is: {length} and the widht is: {width}\n")

print(f"The area of the shape is: {length * width}\n")

if isStudent and not isGraduated:
    print(f"{name} is a student who has NOT graduated yet\n")
else:
    print(f"{name} is NOT a student and has graduated\n")

# Check the values of the booleans
print(f"The variable isStudent is set to: {isStudent}")
print(f"The variable isGraduated is set to: {isGraduated}\n")


if name == nameCopy:
    print('Strings can go in either single or double quotes when defining')
else:
    print("Strings can only go in single quotes\n")

# Quotes can either be escaped or use the other quote 
# the escape character for quotes is either \"TEXT HERE \"
# or \' TEXT HERE \'
print("The man said 'Hello'")
print('The man said "Hello"')
print("The man said \"Hello\"")
print('The man said \"Hello\"')

# the character that cancels the escape characters is the r letter
# this makes it so we don't have to use an escape character every time we
# want a special character
print(r"The file location is C:/User/Documents/YourFile.txt")
print()

# I don't know why you would use this but it exists
# strings can be concatenated and multipled
randomString = "Hello"
randomStringTwo = "World"

# prints 3 copies of "Hello" followed by "World"
# Output: "HelloHelloHelloWorld"
print( 3 * randomString + randomStringTwo + "\n")

# strings next to each other are auto concat.
myString = "Python " "Learning"
print(myString)

# that mechanic is very useful when making long strings
yapping = ("Hello World this is CJ. "
           "I am learning how to code in Python. "
           "This is to demonstrate that strings "
           "can be made on multiple lines when they "
           "are placed next to each other. "
           "This is all stored in 1 variable.")

print(yapping + "\n")

# concat a literal with a var
literal = "Python"
print(literal + " learning\n")


