# This program reads a name and an age for a person, until the name is blank. As each name age pair is entered, store names in a list, and ages in another. Print a list of tuples of paired names and ages.

name = raw_input('Enter name: ')
age = int(raw_input('Enter age: '))

names = []
ages = []

while name != '':
	names = names + [name]
	ages = ages + [age]
	name = raw_input('Enter name: ')
	if name != '':
		age = int(raw_input('Enter age: '))


name_age = []
for a in range(len(names)):
	comb = (names[a],) + (ages[a],)
	name_age = name_age + [comb]
	
print name_age
