print "How old are you?",
# raw_input() allows you to input things, whoo-hoo!
age = raw_input()
print "How tall are you?"
# You can also add a 'prompt' within the parenths.
# Creates a nice little input arrow like so.
height = raw_input('--> ')
print "How much do you weigh?"
weight = raw_input()

# If you use the %r formatter, Python will output hiow it sees fit
# usually including escape characters (in the case of your height.)
print "So you're %r old, %s tall and %r heavy." % (age,height,weight)

# Extra Credit
print "What is your astrological sign?",
sign = raw_input()
print "Oh, what month is that again?",
sign_month = raw_input()
print "Wow, so you were born in %s and that makes you a %s. Cool." %(sign_month,sign)