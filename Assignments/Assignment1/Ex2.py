# This program allows the user to enter two values
# The program uses the function in exercise 1 to convert celcius to fahrenherit of all the values between the input values inclusively
# The result is then printed 


def temp_changer(celcius):            # The function that converts celcius to fahrenherit
	far = 1.8*celcius + 32        # The expression for converting temperature from degree to farenherit
	return far                    # returns the coverted temperature


value1 = int(raw_input('Enter first value: '))  # The first value to be entered by the user
value2 = int(raw_input('Enter second value: ')) # The second value to be entered by the user


print "C", '\t', 'F'		      # This print line, prints the temperature headers

if value1 < value2:
	for celcius in range(value1, (value2+1)):
		print celcius, '\t', temp_changer(celcius)     # '\t', horizontal tab, is just there to create a gap btwn C and F
elif value2 < value1:
	for celcius in range(value2, (value1+1)):
		print celcius, '\t', temp_changer(celcius)
else:
	print value1, '\t', temp_changer(value1)
