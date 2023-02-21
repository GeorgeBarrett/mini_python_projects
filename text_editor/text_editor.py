#import module for arguments
from sys import argv

# breaking down arguments into 2 variables (script is the file name)
script, filename = argv

# this message needs the argument passed in a the terminal (text_editor.txt)
print(f'Do you want to erase {filename}.')
print('If you don\'t want that, hit CTRL C (^C).')
print('If you do want that, hit RETURN.')

input('?')

print('Opening the file...')

# opens the file in 'write mode' (w)
target = open(filename, 'w')

print('Truncating the file. Goodbye!')

# this deletes the content of the text file
target.truncate()

print('Now we can create a new text file with three lines.')

# these three variables store the lines that user inputs
line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

print('I\'m going to write these to the file.')

# these write the inputs into the text file and include the line breaks
# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

target.write(f'{line1}\n{line2}\n{line3}\n')

print('The text file is now complete and closed.')

# this closes the file
target.close()