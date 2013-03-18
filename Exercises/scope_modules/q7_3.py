# The function accepts a list of numbers, and returns their mean.

def mean():
	number = raw_input('Enter number: ')
	num_list = []
	total = 0
	while number != '':
		num = int(number)
		num_list = num_list + [num]
		number = raw_input('Enter number: ')
	for a in num_list:
		total = total + a
	return total/(len(num_list))


print mean()
