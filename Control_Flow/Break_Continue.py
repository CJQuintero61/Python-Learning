# Learning to use break and
# continue in python
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0


# finds the first number from [0,299] that is not 0
# and is divisible by 3, 5, and 7

# the output normally is 105 and 210, which are both divisible by 
# 3 5 and 7 (and are non zero) but ends after finding 105
# because of the break
for i in range(300):
    if((i % 3 == 0) and (i % 5 == 0) and (i % 7 == 0) and (not i == 0)):
        print(f"{i}")
        break


for i in range(100):
    if(i % 3 == 0):
        print(f"{i} is divisible by 3")
        continue
    # when a number divisible by 3 is found, this will not print due
    # to the continue statement
    print(f"{i} is NOT divisible by 3")
