from sys import argv
from os.path import exists

# breaking down argument into three variables
script, from_file, to_file = argv

# printing arguments
print(f'Copying {from_file} to {to_file}')

# i am using vhs for my comments as i can draw parallels with old hardware and python
# inserting the vhs and turning it into an object, which is stored in a variable
# in_file = open(from_file)

# playing the vhs and storing the information as a variable
# in_data = in_file.read()

# i can make lines 12 and 15 into one line
in_data = open(from_file).read()


# i am printing the variable and the 'len' tells me the amount of bytes the file is
print(f'The input file is {len(in_data)} bytes long')

print(f'Does the ouput file exist? {exists(to_file)}')
print('Ready!, hit RETURN to continue or CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print('Alright, all done!')

out_file.close()