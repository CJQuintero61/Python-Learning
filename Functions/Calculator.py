# This file makes a simple calculator program
# to practice functions in python
#
# Developer: CJ Quintero
# Last Updated: 04/23/2025

# imports
import random

# garbage in, garbage out
# this validates that the inputs are numbers
def validateNumber(value):
    return isinstance(value, (int, float))


def add(firstValue, secondValue):
    # both values must be either an integer of a float 
    # then return the sum
    if validateNumber(firstValue) and validateNumber(secondValue):
        return firstValue + secondValue
    # print error message and return 
    else:
        print("Only integers and float values can be added.")
        return 
    
def subtract(firstValue, secondValue):
    # validate 
    if validateNumber(firstValue) and validateNumber(secondValue):
        return firstValue - secondValue
    else:
        print("Only integers and float values can be subtracted.")
        return

def multiply(firstValue, secondValue):
    # validate
    if validateNumber(firstValue) and validateNumber(secondValue):
        return firstValue * secondValue
    else:
        print("Only integers and float values can be multiplied.")
        return
    
def divide(firstValue, secondValue):
    # validate
    if validateNumber(firstValue) and validateNumber(secondValue):
        # divide by zero exception
        if secondValue == 0:
            print("Cannot divide by 0")
            return
        else:
            return firstValue / secondValue
    else:
        print("Only integers and float values can be divided.")



counter = 0
# runs random methods with random integers 
while counter < 20:
    # will randomly choose 1 of the 4 methods
    randomMethod = random.randrange(0, 4)   

    # any integer from [1, 100] (101 is excluded)
    randomValueOne = random.randint(0, 101) 
    randomValueTwo = random.randint(0, 101) 


    # runs the randomly selected method and prints the values with the result
    if randomMethod == 0:
        print("Adding " + str(randomValueOne) + " and " + str(randomValueTwo) + ": " + str(add(randomValueOne, randomValueTwo)))
    elif randomMethod == 1:
        print("Subracting " + str(randomValueOne) + " and " + str(randomValueTwo) + ": " + str(subtract(randomValueOne, randomValueTwo)))
    elif randomMethod == 2:
        print("Multiplying " + str(randomValueOne) + " and " + str(randomValueTwo) + ": " + str(multiply(randomValueOne, randomValueTwo)))
    elif randomMethod == 3:
        print("Dividing " + str(randomValueOne) + " and " + str(randomValueTwo) + ": " + str(divide(randomValueOne, randomValueTwo)))
    else:
        print("An unexpected error has occurred.")

    counter = counter + 1
