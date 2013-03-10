# Write a program that prints out a 'Christmas' tree shape from asterisks. The program should ask the user for the height of the tree, in lines, and the tree should have a stalk of two lines regardless. If the user enters a height, the tree should be printed out, and the user should be prompted for another height until they enter a blank line. 


height_triangle = raw_input('Enter height: ')

while height_triangle != '':
	height = int(height_triangle)
	star = ["*"]*height
	length = len(star) + 1
	b = ' '

	for a in range(1, length):
		print (length-a)*b, '*'*(2*a-1),(length-a)*b 
	for q in range(1,3):
		print length*b+("*")+b*height
	height_triangle = raw_input('Enter height: ')
