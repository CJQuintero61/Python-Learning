# basic arithmetic operations
import math

sum = 10
sum = sum + 5  
print(sum)

difference = 2
difference = difference - 1  
print(difference)

product = 4
product = product * 3
print(product)

quotient = 8
quotient = quotient / 2
print(quotient)

power = 3
power **= 2  # exponentiation (3^2)
print(power)

# using the math library
print(f'The value of pi is: {math.pi}')
print(f'The square root of 16 is: {math.sqrt(16)}')
print(f'The value of e is: {math.e}')
print(f'The sine of 90 degrees is: {math.sin(math.radians(90))}') # using radians
print(f'The sine of 90 degrees using degrees function is: {math.sin(90)}')  # using degrees

# ceiling and floor 
print(f'The ceiling of 4.3 is: {math.ceil(4.3)}')
print(f'The floor of 4.7 is: {math.floor(4.7)}')

# calculate area of a circle
radius = input('Enter a radius of a circle: ')
print(f'The area is: {math.pi * float(radius) ** 2}')

# alternatively store the radius as a float
radius = float(input('Enter a radius of another circle: '))
print(f'The area is: {math.pi * radius ** 2}')

# rouding
print(f'Rounding the area to 3 decimal places: {round((math.pi * radius ** 2), 3)}')
