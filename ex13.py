from sys import argv

script, first, second, third, fourth = argv

# The first entry in a list will always be the script name.
# Even if it is not passed as an argument.
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth