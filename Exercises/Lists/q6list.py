# This program asks the user for their name, and a number, then prints out the user's name a number of times equal to the number they entered.

name = raw_input('Enter name: ')
number = raw_input('Enter number: ')
num = int(number)
count = 1
while count<= num:
	print name
	count = count + 1

