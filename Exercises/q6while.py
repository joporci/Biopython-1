#This program ask the user for a number and then print add the number with 1 up to the number entered by the user.

n = int(raw_input('Enter number: '))
a = 1
b = 0
while a <= n:
	b = b + a
	a = a + 1
print b
