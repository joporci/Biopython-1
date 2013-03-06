a = int(raw_input('First: '))
b = int(raw_input('Second: '))
c = int(raw_input('Third: '))
d = int(raw_input('Fourth: '))
e = int(raw_input('Fifth: '))

if a<b and a<c and a<d and a<e:
	print a
elif b<a and b<c and b<d and b<e:
	print b
elif c<a and c<b and c<d and c<e:
	print c
elif d<a and d<b and d<c and d<e:
	print d
else:
	print e
