#this is a program that when a year is entered it shows its a leap year

y1 = int(raw_input('First: ')) # A variable of the year input


if y1 % 4 == 0: # if the variable divided by 4 leaves a remainder of zero then its a leap year
	print "Year 1 is a Leap year!!!"
else:
	print "Year 1 is not a leap year!!!"
