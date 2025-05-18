# Learning to use lists
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0

# define a simple list
squares = [1, 4, 9, 16, 25]

print(f"Here are the first 5 squares: {squares}\n")

# lists can be appended 
squares = squares + [36, 49, 64, 81, 100]

print(f"Here is the list with more squares: {squares}")

# lists are mutable
squares[5] = 256
print(f"Lists are mutable too: {squares}")

# appending
squares.append(121)
print(f"Here is the list with more squares: {squares}")

# simple assignment in Python always refers to the existing list 
# instead of copying the values
# means copy by reference

# adding good morning to the reference variable, also changes the list variable
list = ["Hello", "World"]
ref = list
ref.append("Good")
ref.append("Morning")
print(f"{list}\n")

# slicing operations return shallow copies
# copies of the original value, not a reference

# here slicing the list then appending to it doesn't change the list variable
slice = list[:3]
slice.append("Afternoon")
print(f"Here is the list: {list}")
print(f"Here is the sliced list: {slice}\n")


# nesting 
shapes = [ 
    ["square", 4],
    ["rectangle", 4],
    ["triangle", 3],
    ["circle", 0],
    ["pentagon", 5]
]

print(f"Here is the nested array: {shapes}")