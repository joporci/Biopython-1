# This program creates my own version of the function random.randrange() by using the function random.randint.



def own_randrange():
	b = int(raw_input('Enter b: '))
	import random
	ans = random.randint(0,b)
	return ans

print own_randrange(1)
	
	
	


