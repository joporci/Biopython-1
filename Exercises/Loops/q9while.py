numbers = raw_input('Enter a number: ')
smallest = numbers
while numbers != '':
	if int(numbers) < int(smallest):
		smallest=numbers
	numbers = raw_input('Enter a number: ')

print smallest, "was the smallest"

