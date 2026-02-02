# this program opens and reads a file and can write to a file

# NOTE:: It is better to use 'with' than file.open() and file.close()
# because 'with' automatically handles closing the file.
import os


# to open a file and read each line
with open('input.txt') as file:
    for line in file:
        print(line, end='') # end='' to avoid double newlines (1 from the file and 1 from print)

print('\n-------------------------------\n')

# to read the content as a whole string
with open('input.txt') as file:
    content = file.read()
    print(content)
    print(f'Length of content: {len(content)}')

print('\n-------------------------------\n')

# reading chuncks at a time
# will read 10 characters at a time
# when there is nothing left to read, it returns an empty string
# and breaks the loop
with open('input.txt') as file:
    chunk_size = 10
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        print(chunk, end='|')  # '|' to indicate chunk boundaries

# writing to a file

# if the file doesn't exist, we can use 'x' mode to create and write
# to a new file
# will throw an error if the file already exists
if ('output.txt') not in os.listdir():
    with open('output.txt', 'x') as file:
        file.write('This file was created using write mode.')
else:
    print('\noutput.txt already exists, skipping creation.')

# using 'w' mode to write to a file
# will overwrite all existing content
with open('test.txt', 'w') as file:
    file.write('Phrase overwritten!')