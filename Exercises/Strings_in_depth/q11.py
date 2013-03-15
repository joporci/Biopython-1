#This program reads in the name, price, and quantity of an item, and stores it in a list of tuples, repeating until a blank product name is entered. It should then print out each item in a nicely formatted manner, using string interpolations.

name = raw_input('Enter name of item: ')
price = float(raw_input('Enter price of item: '))
quantity = int(raw_input('Enter quantity of items: '))

list1 = []

while name != '':
	list1 = list1 + [(name,price,quantity)]
	name = raw_input('Enter name of item: ')
	if name != '':
		price = float(raw_input('Enter price of item: '))
		quantity = int(raw_input('Enter quantity of items: '))

print list1

for a in list1:
	print '%s costs R%.2f per item so we need %i of them' % (a)

