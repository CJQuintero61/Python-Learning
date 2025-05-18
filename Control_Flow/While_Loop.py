# Learning to use while loop
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0

i = 0

# no i++?
while i < 10:
    print(f"The value of i is: {i}")
    i = i + 1
print()

# multiple assignment,
# vars are assigned left to right

# same as 
# a = 0
# b = 1
a, b = 0, 1

while a < 5:
    print(f"A is: {a} and B is: {b}")
    # same as 
    # a = a + 1
    # b = b + 2
    a, b = a + 1, b + 2


# may also print like this
print("The value of A is", a)