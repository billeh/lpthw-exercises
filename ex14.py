from sys import argv

script, user_name, gender = argv
prompt = '--> '

print "Hi %s, you %s, I'm the %s script." % (user_name, gender, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You're also a %r. That's surprising.
""" % (likes, lives, computer, gender)
