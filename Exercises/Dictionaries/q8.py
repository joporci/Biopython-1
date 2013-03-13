# The program reads in names until a blank line is entered, and prints out each unique name and the number of times it was entered.

name = raw_input('Enter name: ')

names = {}
data = []
while name != '':
	data = data + [name]
	names[name] = data.count(name)
	name = raw_input('Enter name: ')


print names

