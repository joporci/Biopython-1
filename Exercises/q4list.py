# This program asks the user to enter a number from 1 to 12 and prints out the name of the corresponding month.

number = raw_input('Enter number: ')

month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

num = int(number) - 1

for a in range(len(month)):
	if num == a:
		print month[a]
	
