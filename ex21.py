def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a*b

def divide (a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."
# To solve these by hand work them out from the INSIDE outwards!
what = add(age, subtract(height,multiply(weight,divide(iq,2))))
no = subtract(height,add(iq, multiply(weight,divide(age,3)))) 
print "That becomes: ", what, "Can you do it by hand?"
print "Your new equation is", no, "... Why bother doing it by hand!?"