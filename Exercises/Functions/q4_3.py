# The function accepts a single integer parameter, and returns True if the number is prime, otherwise False.

def prime(number):
	s = []
	for a in range(2, number):
		if number % a == 0:
			s = s + [a]		
	
	if s == []:
		return True
	else:
		return False
		
				

number = int(raw_input('Enter integer: '))

print prime(number)

