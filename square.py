# A function to square any number
def sq(x):
	#y = x^2
	y = x**2
	return y

# For x values from 0 to 19
for x in range(20):
	# Print x and its squared value
	print(str(x) + "^2 = " + str(sq(x)))
