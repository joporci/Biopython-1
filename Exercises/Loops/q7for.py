num1 = raw_input('Enter first number: ')
num2 = raw_input('Enter second number: ')

x = int(num1)
y = int(num2)
total = 0

if x < y:
	y = y + 1
	for number in range(x, y):
		total = total + number

if y < x:
	x = x + 1
	for number in range(y, x):
		total = total + number

print total
