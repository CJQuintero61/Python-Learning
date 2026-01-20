# for strings you can index individual characters using 3 different methods
# [start : end : step]
# this means " start at index 'start', go up to but not including index 'end', taking steps of size 'step' "

my_string = "Hello, World!"
# print every other character from index 0 to index 12
print(my_string[0:12:2])  # Hlo ol which doesn't include the !

# you can also omit the start, end, or step values
# print every character from the beginning to index 5
print(my_string[:5])  # Hello


# print every character from index 7 to the end
print(my_string[7:])  # World!

# print every character in the string with a step of 3
print(my_string[::3])  # Hl r!

# you can also use negative indexing to start from the end of the string
# print every character from index -1 to index -6
print(my_string[-6:])  # World! 


# to reverse a string use a step of -1
print(my_string[::-1])  # !dlroW ,olleH

