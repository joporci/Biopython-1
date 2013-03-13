#This program accepts a list of numbers terminated by a blank line. Prints out the entered numbers as elements of a tuple, in the order they were entered.

number = int(raw_input('Enter number: '))

numberlist = ()

while number != '':
	num = int(number)
	numberlist = numberlist + (num,)
	number = raw_input('Enter number: ')

print numberlist
