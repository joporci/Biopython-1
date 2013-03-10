# This program prints out the multiplication table for 1 to 10

for i in range(1, 11):
	for j in range(1, 11):
		y = i*j
		print y, '\t',
	if j ==10:
		print ''
