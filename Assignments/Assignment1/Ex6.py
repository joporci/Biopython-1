#The program ask for information about a city(name, population, is capital?, income) and prints a message indicating if the city is a metropoly and if not why is not considered such as.

name = raw_input('Enter city name: ')			# City name
population  = int(raw_input('Enter population: '))	# Population of that city
capital = raw_input('Is it capital: ')			# Is that city a capital: The answer should be y or n
income = int(raw_input('Income: '))			# The average income per year

if (capital == 'y' and population > 100000) or (population > 200000 and income > 720000000):	# Test if the city is a metropoly
	print name, 'is a metropolitan.'

elif population < 100000:			#if not a metropoly, check if population is the cause
	print name, 'is not metropolitan because of small population'

elif capital != 'y' and population < 200000:	#if not metropoly, check capital and low population causing
	print name, 'is not metropolitan because city is not capital and the population low.'

else:
	print name, 'is not metropolitan because the average income is low.'	#the average income is too low



	
	
