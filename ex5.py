name = 'Billy'
age = 21
height = 67 # in inches
weight = 140 # in pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
height_meters = height/float(12)*0.304
weight_kilo = weight/float(2.2)

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, he's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# Tricky line incoming:
print "If I add %d, %d, and %d I get %d." % (age, height,weight,age + height + weight)

print "He's %f feet, just so you know." %(float(height)/12)
print "%f meters for you Europeans." %(height_meters)
print "Wow, only %f kilograms. Makes you look skinny!" %(weight_kilo)