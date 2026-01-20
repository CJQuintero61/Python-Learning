# Getting user input and displaying a greeting message
user_name = input('Enter your name: ')
print(f'Hello {user_name}!')

# User input is always stored as a string
age = input('Enter your age: ')
print(f'You are {age} years old.')
print(f'Type of age: {type(age)}')

# doing math with user input
length = input('Enter the length of the rectangle: ')
width = input('Enter the width of the rectangle: ')

# must cast to int or float before doing math
area = int(length) * int(width)
print(f'The area of the rectangle is: {area}')