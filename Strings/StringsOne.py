# String basics
#
# author: CJ Quintero
# last updated: 04/21/2025

# fields
greeting = "Hello CJ"

# do not do this
multiLineString = """This is a multiline string
this is on a new line
this is the third line
last line"""

stringExample = "Hello World"

# literals
print("Hello World!")

# quotes in quotes
# can use either single or double quotes for outer string 
print("My name is 'CJ'")
print('My name is "CJ"')
print("\n")

print(greeting)
print("\n")

# nasty 
print(multiLineString)
print("\n")

# print a single character
# string arrays are 0 based as usual
print(stringExample[1])
print("\n")

# use a loop 
for character in stringExample:
    print(character)

print("\n")

for character in "Banana":
    print(character)
