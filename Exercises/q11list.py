# this program asks the user for a number from 1 to 12, and then prints out the name of corresponding month, and the number of days in that month, in the form: "January has 31 days."

number = raw_input('Enter number: ')

month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

long_months = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
short_months = ['april', 'june', 'september', 'november']

num = int(number) - 1

for a in range(len(month)):
	if num == a:
		if month[a] in long_months:
			print month[a], "has 31 days."
		elif month[a] in short_months:
			print month[a], "has 30 days."
		else:
			print month[a], "has 28 days."
