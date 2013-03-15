# This program modify the answer to question 11 to use products from a dictionary of product codes mapped to product descriptions. Invalid codes should print a warning, and product codes should be integers. The print out at the end should print the full name of the item, followed in brackets by it's code, as well as price and quantity.

name = raw_input('Enter name of item: ')
price = float(raw_input('Enter price of item: '))
quantity = int(raw_input('Enter quantity of items: '))
code = int(raw_input('Enter code of item: '))

dic = {}


while name != '':
	dic[code] = [name,price,quantity]
	name = raw_input('Enter name of item: ')
	if name != '':
		price = float(raw_input('Enter price of item: '))
		quantity = int(raw_input('Enter quantity of items: '))
		code = int(raw_input('Enter code of item: '))

	

print "looking for something, follow the instruction"

item_id = int(raw_input('Enter item id: '))

codes = dic.keys()

if item_id in codes:
	print item_id, dic[item_id]
else:
	print "Warning: id not found: check from the entire list"
	print dic
	



