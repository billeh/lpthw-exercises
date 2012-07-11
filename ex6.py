x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# The modulo (%) passes the string values into the formatters.
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

# The format character r and s both handle strings.
print "I said: %r." % x
# The contents of the variable 'y' get passed to %s. 
print "I also said: '%s'." % y

hilarious = False

# The the variable to print for %r is in line 19. This works.
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# This concatenates the two strings in the above declarations.
print w + e