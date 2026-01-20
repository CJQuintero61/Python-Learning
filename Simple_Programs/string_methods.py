# Various functions that can be used on strings
name = "Johnny Bravo show"
print(name.upper())          # Convert to all caps
print(name.lower())          # Convert to all lowercase
print(name.title())          # Convert to title case (each word capitalized)
print(name.replace("Bravo", "Test"))  # Replace a substring with another substring

# find the position of a substring
# will return -1 if the substring is not found
first_space_index = name.find(" ")
print(f'The first space is at index: {first_space_index}') # uses 0 based indexing

# validating digit inputs
age = input("Enter your age: ")

if age.isdigit():
    print(f'You are {age} years old.')
else:
    print('You entered characters that aren\'t digits!')

# isalpha checks if all characters are letters
first_name = input("Enter your first name: ")

if first_name.isalpha():
    print(f'Hello, {first_name}!')
else:
    print('Your name can only contain letters!')

# counting the occurances of a substring
phrase = "The rain in Spain stays mainly in the plain"
count_in = phrase.count("in")
print(f'The substring "in" occurs {count_in} times in the phrase.')

# replace substring example
phone = '123 456 7890'
phone = phone.replace(' ', '-')  # replace spaces with dashes
print(f'Formatted phone number: {phone}')