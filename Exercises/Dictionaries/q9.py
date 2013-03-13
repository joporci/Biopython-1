# This program reads strings until a blank line is encountered. For each string entered, treat the portion of the string up to the first colon (or the entire string if no colon is present) as a key name, and everything after the first colon as a value. If the key portion has been entered before, print out the old value paired with that key, and then change the value to the newly entered one. After the blank line, print out a neat list of key value pairs.

string = raw_input('Enter strings: ')

dic = {}

while string != '':
	if ':' in string:
		a = string.index(':')
		if a != (len(string)):
			key = string[:a]
			value = string[(a+1):]
		else:
			key = string
			value = ''
	
	else:
		key = string
		value = 'no colon'

	if key in dic.keys():
		print key, dic[key]

	dic[key] = value
	string = raw_input('Enter strings: ')
	
	
print dic

