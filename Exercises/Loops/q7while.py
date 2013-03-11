#This program ask the user for a number and then print add the number with 1 up to the number entered by the user.

x = int(raw_input('Enter first number: '))
y = int(raw_input('Enter second number: '))
b = 0
if x < y:
	while x <= y:
		b = b + x
		x =x + 1 
else:
	while y <= x:
		b = b + y
		y = y + 1

print b
