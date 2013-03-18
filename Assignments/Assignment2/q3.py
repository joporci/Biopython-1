#  This program modify the previous code in such a way that the user can input as many sequences as he desires, and the tuples now have a 5th position that counts any other character different to a valid nucleotide.


nuc = raw_input('Enter the nucleotide sequence: ')	# This allows the user to enter a sequence of choice
nucleotides = []					# An empty list that will be used to store the sequences


while nuc != '':					# The loop allows to enter as many sequences as desired
	nucleotides = nucleotides + [nuc]		# the nucleotide sequence is enclosed in brackets so it can be added in the 
	nuc = raw_input('Enter the nucleotide sequence: ')


sequences = []

for seq in nucleotides:			# This loop is allows the change of any base that is noa a, c,t, g into a star for analysis purpose
	nuc1 = ''
	for char in seq:
		if char == 'a' or char == 'A':
			nuc1 = nuc1 + char
		elif char == 'c' or char == 'C':	
			nuc1 = nuc1 + char
		elif char == 't' or char == 'T':	
			nuc1 = nuc1 + char
		elif char == 'g' or char == 'G':	
			nuc1 = nuc1 + char
		else:
			nuc1 = nuc1 + '*'	# This command changes the unknown base into a star
	sequences = sequences + [nuc1]


list1 = []				# list1 is an empty list that is going to be used to store the count of each base
for x in sequences:			# The loop repeats each sequence in the nucleotide sequence
	a = x.count('a') + x.count('A')	# a is a variable that has the value of sum of both lower and upper-case a
	t = x.count('t') + x.count('T')	# t is a variable that has the value of sum of both lower and upper-case t
	g = x.count('g') + x.count('G')	# g is a variable that has the value of sum of both lower and upper-case g
	c = x.count('c') + x.count('C')	# c is a variable that has the value of sum of both lower and upper-case c
	char = x.count('*') 
	list1 = list1 + [(a,t,g,c,char)]	# list1 is will b the list of the counts of the bases in each sequence saved in a tuple

	
a = 1						# This is a sequence counter
for tup in list1:
	print 'SEQUENCE',a, '\b:', nucleotides[a-1]
	print ' A','|',tup[0]
	print '-------'
	print ' T','|',tup[1]
	print '-------'
	print ' G','|',tup[2]
	print '-------'
	print ' C','|',tup[3]
	print '-------'
	print ' *','|',tup[4]
	print '-------'
	a = a + 1

