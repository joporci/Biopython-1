# The program reads in names until a blank line is encountered, after which it prints out an English style list, i.e. a comma separated list, where the last name is preceded by the word 'and' instead of a comma.

name = raw_input('Enter name: ')

list1 = []

while name != "":
	list1 = list1 + [name]
	name = raw_input('Enter name: ')

data = list1[-2] +' and ' + list1[-1]

list1[-2:] = [data]

print list1


