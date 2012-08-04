print """You enter a dark room with three doors. 
Do you go throught door #1 or door #2 .. or DOOR #3!?"""

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do?!"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else: 
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Dude, your eyes are so red."
	else:
		print "Kaliedoscope eyes. Great job!"

elif door =="3":
	print "There's a really smelly guy in here. Smells like fart."
	print "1. \"Dude, lay off the burritos.\""
	print "2. Poke him with a churro."
	print "3. Demand he cease gas leakage."

	diablo = raw_input("> ")

	if diablo == "1" or diablo == "2":
		print "He releases yet another steamy bath of fart. You black out."
	elif diablo == "3":
		print "Shouldn't have opened your mouth. You are force-fed his burrito."
	else: 
		print "Yuck, just pick another door next time."	
else:
	print "You have been eaten by a grue."		