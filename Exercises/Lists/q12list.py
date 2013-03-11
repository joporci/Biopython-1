# Modify your answer to question 10 from "Flow Control: Conditionals",print out the numbers from 1 to 10 by which a user entered number is divisible, to use a for loop instead of multiple if statements.

number = int(raw_input('Enter a number: '))

for a in range(1, 11):
	if number % a == 0:
		print a

