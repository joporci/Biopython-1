# This program asks the user for the height of a triangle. If a blank line is entered, the program finishes, otherwise it prints out a right handed triangle, with the right angle in the top right, made of asterisks ('*') of a height equal to the number entered.

height_triangle = raw_input('Enter height: ')

while height_triangle != '':
	height = int(height_triangle)
	star = "*"*height
	length = len(star) + 1
	b = ' '
	for a in range(1, length):
		if a == 1:
			print '*'*(length - a)
		else:
			print (a-2)*b,'*'*(length - a)
	height_triangle = raw_input('Enter height: ')
