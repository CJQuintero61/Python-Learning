# This file practices data types
# 
# author: CJ Quintero
# last updated: 04/21/2025

# Strings
firstName = "Christian"
lastName = "Quintero"

# ints
age = 20
graduationYear = 2027

# floats
PI = 3.14159
priceOfChips = 2.99

# bools - must be uppercase when assigning 
isStudent = True
isGraduateStudent = False


# format output
print(f"Hello {firstName} {lastName}")

# or print like normal by concatenating strings
print("Hello " + firstName + " " + lastName)
print("\n")


# print values
# note: must cast the type to a string to concatenate output like this
print("I am " + str(age) + " years old")
print("I plan to graduate in " + str(graduationYear))
print("\n")


# conditional statements
if isStudent:
    print("I am a student")
else:
    print("I graduated! (NOT YET!)")
    
print("\n")


# conditional statements
if isGraduateStudent:
    print("Welcome to grad school!")
else:
    print("Graduate first")

print("\n")

print("PI is approx. equal to: " + str(PI))
print("Chips cost: " + str(priceOfChips))