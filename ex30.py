people = 100
cars = 40
buses = 15

# if cars are greater then people
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "There's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."	
else:
	print "Fine, let's just stay home then."

if cars + buses < people:
	print "This is armageddon!"