name1 = raw_input('First: ')
name2 = raw_input('Second: ')
name3 = raw_input('Third: ')

if name1<name2 and name2<name3:
	print name1, name2, name3 
elif name1<name2 and name3<name2:
	print name1, name3, name2
elif name2<name1 and name1<name3:
	print name2, name1, name3
elif name2<name1 and name3<name1:
	print name2, name3, name1
elif name3<name1 and name1<name2:
	print name3, name1, name2
else:
	print name3, name2, name1
