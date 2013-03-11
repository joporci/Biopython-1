# This program asks for 7 cities and display: the list of the metropolis, which is the metropoly with less population, wich is the city that is not a metropoly with more income, which capital city has the biggest population

name = raw_input('Enter city name: ')			# city name
population  = int(raw_input('Enter population: '))	# the population of that city
capital = raw_input('Is it capital: ')			# check if the city is capital or not: y = yes, n = no
income = int(raw_input('Income: '))			# the average income of the city per year

if (capital == 'y' and population > 100000) or (population > 200000 and income > 720000000):	# conditions that satisfies a metropoly
	less_pop = population									# less_pop - less population, starting value
	less_pop_name = name									# the name of the city with less population
	more_income = 0										# the starting value for more_income
	more_income_name = "no city"								# the name of the city with more income
	metro = [name]

else:
	less_pop = 9999999999999999999999999999999	# if not metropoly starting value for city pop
	less_pop_name = "no city"			# starting name for the city with less pop
	more_income = income				# more_income, starting value
	more_income_name = name				# name of the city with more income


if capital == 'y':				# if the city is a capital city
	cap_pop = population			# then the population of that city is cap_pop
	cap_pop_name = name			# the variable name is given

else:
	cap_pop = 0				# if not capital, starting value is 0
	cap_pop_name = 'no city'		# the variable name if the starting city is not capital



for a in range(1, 7):				# the loop repeats 6 times asking the city details
		
	name = raw_input('Enter city name: ')
	population  = int(raw_input('Enter population: '))
	capital = raw_input('Is it capital: ')
	income = int(raw_input('Income: '))
	
	if (capital == 'y' and population > 100000) or (population > 200000 and income > 720000000):
		if population < less_pop:		# compares the population value with the previous value
			less_pop = population		# if true gives a new value for less_pop
			less_pop_name=name		# and a new name for the city with less pop
		metro = [metro] + [name]


		if capital == 'y':			# if city is capital
			if population > cap_pop:	# compares the population of the city with the previous value
				cap_pop = population	# if true gives a new value for cap_pop
				cap_pop_name = name	# and a new name for the city with cap_pop

		
	else:						# if not metro
		if income > more_income:		# compares the city income with the previous income
			more_income = income		# if true gives more_income a new value
			more_income_name = name		# and a new name


		if capital == 'y':			# same description as above (line 40 to line 43)
			if population > cap_pop:
				cap_pop = population
				cap_pop_name = name
	

print 'The cities that are metropolytans are:', metro
print less_pop, less_pop_name			# displays the output of a metro with less_population and the name of that city
print cap_pop, cap_pop_name			# displays the output of a capital city with more population and the name of that city
print more_income, more_income_name		# displays the output of non-metro city with more income




