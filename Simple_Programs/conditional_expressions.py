# conditional expressions are ternary operators
# often used to make one liners for simple if-else statements
# sytas: variable if condition else variable

price = 11.99 

# apply a 10% discount if the price is greater than $10
# else use the original price
final_price = price * .9 if price > 10 else price

# with money, we use 2 decimal places
print(f'The final price is: {round(final_price, 2)}')

# another example
access_level = 'admin'

clearance = True if access_level == 'admin' else False

if clearance:
    print('Access granted')
else:
    print('Access denied')