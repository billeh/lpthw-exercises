from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C."
print "If you want to do that, hit return!"

raw_input("?")

print "Opening the file..."
target = open(filename,'w+') # mode 'w+', for writing (and updating so later we can read).

print "Truncating the file. Goodbye!"
target.truncate() # this kills the file (do not actually need this line when opening with w(+))

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

lines = line1+"\n"+line2+"\n"+line3+"\n"
target.write(lines)

print target.read()
target.close() # closes the file.