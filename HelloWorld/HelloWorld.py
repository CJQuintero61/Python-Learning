# This file prints basic stuff
# 
# author: CJ Quintero
# last updated: 04/20/2025
print("Hello World");
print("This is my first python file!");

# strings
myFirstVariable = "Hello CJ!\nWelcome to the Python Language!";
firstName = "CJ";
lastName = "Quintero";

# prints the variable
print(myFirstVariable);

# formats the output
print(f"This is how you format output {firstName}");
print(f"{firstName} {lastName}");

# integers
age = 20;
print(f"I am {age} years old at the time of writitng this.");

# floats 
PI = 3.14159;
print(f"here is PI: {PI}");

# bools
# True/False must be capitalized when assigning 
isTrue = True;

if isTrue:
    print("This is true");
    print("This is the language of the snakes");
    print("NO SEMICOLONS ARE NEEDED EITHER")
else:
    print("This is not true");
    print("This is also not true");
    print("No curly braces needed in python");

