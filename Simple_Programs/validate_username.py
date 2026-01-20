# Validate a username
# the username must not exceed 12 characters
# there can not be any spaces in the username
# there can not be any digits in the username
# the username can not contain special characters

username = input("Enter a username: ")

# check length
if len(username) > 12:
    print("Username must not exceed 12 characters.")
elif username.find(' ') != -1:  # will return -1 if no spaces found
    print("Username must not contain spaces.")
elif not username.isalpha():  # isalpha returns True if all characters are letters
    print("Username must only contain letters.")
else:
    print(f'Username "{username}" is valid!')