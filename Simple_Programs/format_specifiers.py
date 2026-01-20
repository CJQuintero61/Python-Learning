# Format specifiers 

# formatting floating point numbers
import math

pi = math.pi
print(f'Pi rounded to 5 decimal places: {pi:.5f}')

# zeros can be padded to the right of the decimal point
# if the number has fewer decimal places than specified
padding = 1.2
print(f'Padded number: {padding:.5f}')

# if you remove the decimal, that specifies the total width of the number
# including blank space, whole numbers, and decimal places
width_example = 1.23
print(f'Width specified number: {width_example:8}')

# you can use place a 0 before the width to pad with zeros instead of spaces
# on the left of the number
zero_padding = 1.23
print(f'Zero padded number: {zero_padding:08}\n')


# justification uses < for left, ^ for center, and > for right
left_justified = 1.23
center_justified = 1.23
right_justified = 1.23
print(f'Left justified: {left_justified:<10}')
print(f'Center justified: {center_justified:^10}')
print(f'Right justified: {right_justified:>10}\n')

# to force a sign to appear, use + before the width
positive_number = 42
negative_number = -42
print(f'Positive number with sign: {positive_number:+}')
print(f'Negative number with sign: {negative_number:+}')

# you can also use commas to separate thousands
large_number = 100000000
print(f'Large number with commas: {large_number:,}')

# combining multiple format specifiers
# zero padding the left, right justifying, using 15 total spaces, 
# a thousanths separator, and rounding to 2 decimal places
combined_example = 1234.56789
print(f'Combined specifiers: {combined_example:0>15,.2f}')