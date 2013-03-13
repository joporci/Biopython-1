# This program reads a name and an age for a person, until the name is blank. Once all names have been present the user with an option to list the entered people in alphabetical order, or in descending age order. For either choice, list each person's name followed by their age on a single line. Make sure you output the correct age for the correct person.

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
	comb = [names[a]] + [ages[a]]
	name_age = name_age + [comb]


to_do = raw_input('What do you want to do? Type alphabetically or descending? ')
descending = [['test', 1000]]
if to_do == 'alphabetically':	
	name_age.sort()
	name_age = str(name_age)
	print name_age
else:
	for a in range(len(name_age)):
		if name_age[a][1] < descending[a][1]:
			descending = descending + name_age[a]
		else:
			descending = name_age[a] + descending
	print descending

