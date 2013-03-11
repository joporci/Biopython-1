x=3
y=3
for i in range(1,6):
	for j in range(1,6):
		if (i-1) == y and (j-1) ==x:
			print 'x',
		else:
			print '#',
		if j == 5:
			print ''

