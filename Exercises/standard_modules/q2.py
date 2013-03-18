# This program create my own version of the function random.randint() by using the function random.choice. Hint: Use the range() function.

def own_randint(a,b):
	a = int(raw_input('Enter a: '))
	values = range(a+1)
	import random
	x = random.randchoice(values)
	return x

print own_randint(1,9)
