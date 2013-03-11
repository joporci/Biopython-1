floats = raw_input('Enter floats: ')
count = 0
total = 0.0
mean = 0
summation = 0
while floats != '':
	count = count + 1
	total = total + float(floats)
	floats = raw_input('Enter floats: ')
	if floats == '':
		question = raw_input('what do u want? ')
		if question == 'mean':
			mean = total/count
			print "The mean of the floats entered is", mean
			floats = raw_input('Enter floats: ')
		if question == 'sum':
			summation = total
			print "The sum of floats entered is", summation
			floats = raw_input('Enter floats: ')
		if question == 'quit':
			print "The program is terminated"
