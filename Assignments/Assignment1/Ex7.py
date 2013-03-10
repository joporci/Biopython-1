# This program asks for information about a city(name, population, is capital?, income) and prints a message indicating if the city is a metropoly and if not why is not considered such as.

for a in range(1, 8):
	name = raw_input('Enter city name: ')
	population  = int(raw_input('Enter population: '))
	capital = raw_input('Is it capital: ')
	income = int(raw_input('Income: '))
	
	if (capital == 'y' and population > 100000) or (population > 200000 and income > 720000000):
		print name, 'is a metropolitan.'
	elif population < 100000:
		print name, 'is not metropolitan because of small population'
	elif capital != 'y' and population < 200000:
		print name, 'is not metropolitan because city is not capital.'
	else:
		print name, 'is not metropolitan because the average income is low.'




