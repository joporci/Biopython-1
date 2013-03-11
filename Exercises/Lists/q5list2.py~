# This program asks the user to enter a sequence of up to 5 x:y coordinates with both x and y in the range 0 to 4, ending their sequence entry by providing a blank line for the x coordinate. Then display a five by five grid of '#' characters, with the points in the grid entered by the user left blank. Assume x increases from left to right, and y increases from top to bottom.

print "NB: x and y must be in the range of 0 and 4: 'TAKE NOTE!!!!'"

x_cod = raw_input('Enter x coordinates: ')	
y_cod = raw_input('Enter y coordinates: ')

x = int(x_cod)
y = int(y_cod)

list1 = [[x,y]]

if x<5 and y<5:
	while x_cod != '':
	
		x = int(x_cod)
		y = int(y_cod)

		x_cod = raw_input('Enter x coordinates: ')
		y_cod = raw_input('Enter y coordinate: ')

		list1 = list1 + [[x,y]]


	for i in range(1,6):
		for j in range(1,6):
			if [(j-1), (i-1)] in list1:
				print ' ',
			else:
				print '#',
			if j == 5:
				print ''
else:
	print "Error either x or y is out of range, check yo numbers and start again"

