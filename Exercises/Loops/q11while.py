names = raw_input('Enter names: ')
first = names
last = names
shortest = names
longest = names

while names != '':
	if names < first:
		first = names
	if names > last:
		last = names
	if len(names) < len(shortest):
		shortest = names
	if len(names) > len(longest):
		longest = names
	names = raw_input('Enter names: ')

print "The first name alphabetically is", first
print "The last name alphabetically is", last
print "The shortest name is", shortest
print "The longest name is", longest
	
