# This program prints out the multiplication table for 1 to 10

for i in range(1, 11):			# repeats from 1 -10
	for j in range(1, 11):		#nested loop, also repeats 1_10
		y = i*j			# y is a variable that is found by multiplying i and j
		print y, '\t',		# displays the output of y with a horintal tab after every result

	if j ==10:			#if j = 10, 
		print ''		# displays an empty string and start printing on a newline
