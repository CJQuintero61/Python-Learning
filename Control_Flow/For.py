# Learning to use for loops
# these are similar to enhanced for loops
#
# author: CJ Quintero
# last updated: 05/12/2025
# version: 1.0

list = ["Hello", "good", "morning", "user"]

# aka an enhanced for loop in other languages
# prints the list item then the length of that item, for each item in list 
for str in list:
    print(f"{str} has {len(str)} characters in it")


# changing a list
# changes the values to their cubes 
values = [1, 2, 3, 4, 5]
for i in range(len(list) + 1):
    values[i] = (i + 1) ** 3

print(f"Here is the new list: {values}")

# make a list with only 5
list2 = [5]

# for 19 times, append the last item + 5
# to make a list counting by 5's until 100
for i in range(19):
    list2.append(list2[i] + 5)

print(f"here is the 5's list: {list2}\n")

# will loop for 10 times, starting with i = 0, until i < 10 s
# so it will stop at i = 9
for i in range(10):
    print(f"The value of i is {i}")