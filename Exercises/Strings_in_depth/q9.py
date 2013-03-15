# This program print a column of numbers so the line up right justified for convenient addition

number = raw_input('Enter number: ')
store = []
while number != '':
	store = store + [number]
	number = raw_input('Enter number: ')


for a in store:
	print a.rjust(3)
	
