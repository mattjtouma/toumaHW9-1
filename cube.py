# Function to cube numbers
def cb(x):
	y = x**3
	return y

# For x is 0 to 19
for x in range(20):
	# If x is even it will have a remainder of zero
	if (x % 2) == 0:
		# Print just x
		print(x)
	# Otherwise, x must be odd
	else:
		# Print the cube of x
		print(cb(x))
