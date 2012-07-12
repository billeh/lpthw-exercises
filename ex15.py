# from sys import argv

# script, filename = argv

# # Opens the filename passed in and assigns it to the variable txt.
# txt = open(filename)

# # Prints out the name of the file.
# print " Here's your file %r:" % filename
# # Reads the text from file and prints it.
# print txt.read()

#print "Type the filename again:"
# Assigns the filename to another variable.
#file_again = raw_input("> ")
# # Opens the file and assigns it to another variable.
#txt_again = open(file_again)

# Opens, reads and prints the file.
#print txt_again.read()

print "Enter a filename to print:"
filename = raw_input("> ")
txt = open(filename)
print txt.read()
close (txt)
