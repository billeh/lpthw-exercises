formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two","three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	# this line will print with double 
	# quotes because it contains a single quote		
	"But it didn't sing.", 
	"So I said goodnight."
)