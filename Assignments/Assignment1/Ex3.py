# This program creates a function that given the values of the slope and the Y intercept can calculates the Y-Axis value of a given X for a straight line.
# slope = (change in y)/(change in x)
# equation of a straight line is y = mx + b

slope = int(raw_input('Enter slope: '))
b = int(raw_input('Enter Y-Intercept: '))
x = int(raw_input('Enter x-value: '))

def calculateY(x):	      # This function calculates the y value of a straight line
	y = slope*x + b       # The equation of a straight line
	return y

calculateY(x)
