# This file is for learning if/else blocks
#
# author: CJ Quintero
# last updated: 04/21/2025


# fields
isStudent = True
isLearningPython = True
value = 42


# python uses indents to identify block scope
# this is the same as using curly braces without the braces
if isStudent:
    print("I am a student")
else:
    print("I am not a student")


# python uses "elif" as a keyword for "else if"
if 5 > 10:
    print("5 is greater than 10")
elif 5 == 5:
    print("5 equals 5")
else:
    print("5 is greater than 10")


# logical AND
# python uses "and" keyword for "&&"" in logic 
if 1 > 0 and 2 > 1:
    print("1 > 0 AND 2 > 1")
else:
    print("Logic error")

# logical OR
# python uses "or" keyword for "||" in logic
if 1 < 0 or 2 > 1:
    print("Either 1 is less than 0 OR 2 is greater than 1")
else:
    print("Logic error")

# logical NOT
# python uses "not" keyword instead of "!"
if not 1 < 0:
    print("1 is greater than 0")
else:
    print("1 is less than 0")


if isStudent and isLearningPython:
    print("I am a student learning python")
    print("both true")
else:
    print("I am not a student or I am not learning python")
    print("AND is strong")

print("\n\n")


# nested if/else statements
if value > 10:
    print(str(value) + " is greater than 10")

    if value > 20:
        print(str(value) + " is greater than 20")

        if value > 40:
            print(str(value) + " is greater than 40")
        else:
            print(str(value) + " is not greater than 40")
                  
    else:
        print(str(value) + " is not greater than 20")

else:
    print(str(value) + " is not greater than 10")


# pass statement is the same as continue 
# breaks out of the current block to run the next stuff
if 10 > 5:
    pass
else:
    print("Exiting...")
    exit()

print("If you see this print, then the pass statement ran")

# I do not use ternary operators in any language
# :)
