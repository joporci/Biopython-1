# This program accepts a single integer parameter, and returns a list of the prime numbers from 2 to the number.

import q4_3

number = int(raw_input('Enter integer: '))

list1 = []
for a in range(2,number+1):
	if q4_3.prime(a) == True:
		list1 = list1 + [a]

print list1

