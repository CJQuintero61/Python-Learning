# while loops
# This program prints the first 10 numbers in the Fibonacci sequence
# using a while loop

# initial values
x = 0
y = 1
z = 0           # the sum of the previous two numbers
count = 0       # loop counter
limit = 10      # number of Fibonacci numbers to print

while count < limit:
    if count == 0:
        print(f'{x}')
    elif count == 1:
        print(f'{y}')
    else:
        z = x + y
        print(f'{z}')
        x = y
        y = z
    
    count += 1