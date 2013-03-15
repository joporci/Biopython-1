# This function accepts a single integer parameter, and returns a list of the prime numbers from 2 to the number.

def prime(number):
	s = []
	for a in range(number):
		if a > 1:
			if number % a == 0:
				s = s + [a]	
	
	if s == []:
		return True
	else:
		return False


number = int(raw_input('Enter integer: '))

list1 = []
for a in range(2,number+1):
	if prime(a) == True:
		list1 = list1 + [a]

print list1

			
