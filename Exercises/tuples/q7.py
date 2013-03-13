# This program accepts a list of numbers terminated by a blank line, and stores the result in a tuple, a. Repeat the process to form a second user inputted tuple, b, making sure there are the same number of elements in b as in a. Print out the result of the mathematical addition (not concatenation) of the two tuples as a tuple.

number1 = int(raw_input('Enter numbers for a: '))

a = ()

while number1 != '':
	num1 = int(number1)
	a = a + (num1,)
	number1 = raw_input('Enter numbers for a: ')




number2 = int(raw_input('Enter numbers for b: '))

b = ()

while number2 != '':
	num2 = int(number2)
	b = b + (num2,)
	number2 = raw_input('Enter numbers for b: ')

total = ()
if range(len(a)) == range(len(b)):
	for value in range(len(a)):
		add = a[value] + b[value]
		add1 = (add,)
		total = total + add1
	print total	

else:
	print "can't add, the number of elements are different!!!"




