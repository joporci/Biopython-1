# This function accepts a list of numbers, and returns the sum of their squares

def sum_sq():
	number = raw_input('Enter number: ')
	num_list = []
	total = 0
	while number != '':
		num = int(number)
		num_list = num_list + [num]
		number = raw_input('Enter number: ')
	for a in num_list:
		total = total + (a**2)
	return total


print sum_sq()
