from sys import argv

script, input_file = argv

def print_all(f):
	print f.read() # Prints all lines

def rewind(f):
	f.seek(0) # 'Rewinds' the file. 0 is the offset that places the pointer at the beginning of the file
# Current line (below) is used as a parameter and becomes 'line_count' in this function.
def print_a_line(line_count, f):
	print line_count,f.readline() # Prints the line number and then the line itself.

current_file = open(input_file) # Opens the file passed in as an arg.

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

print "Let's print these three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # Equals 2
print_a_line(current_line, current_file)

current_line += 1 # Equals 3
print_a_line(current_line, current_file)
