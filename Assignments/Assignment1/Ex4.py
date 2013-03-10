# This program is the modification of the previous algorithm that alternates the values of X from 1 to 10 and calculate each corresponding Y.


m = int(raw_input('Enter slope: '))
b = int(raw_input('Enter Y-Intercept: '))

def calculateY(x):	      # This function calculates the y value of a straight line
	y = m*x + b       # The equation of a straight line
	return y

print "The results for the linear equation Y=mX+b with m =", m, "and b =", b, "are:"
print "X", '\t', "Y"

for x in range(1, 11):
	print x, '\t', calculateY(x)
	

