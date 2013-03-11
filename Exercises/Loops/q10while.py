numbers = raw_input('Enter a number: ')
total = 0 #to store cumulative numse
count = 0 # to use when calculating the average  (average=total/count)
while numbers != '':
	count = count+1
	total = total + int(numbers)
	numbers = raw_input('Enter a number: ')

print total/count, " is the average"

