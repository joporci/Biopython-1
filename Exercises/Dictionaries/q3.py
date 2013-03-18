# This program modify the first question's code in such a way that the user can input as many sequences as he desires, and the tuples now have a 5th position that counts any other character different to a valid nucleotide and then prints the results in a tabular way.

nuc = raw_input('Enter the nucleotide sequence: ')
nucleotides = []

while nuc != '':
	nucleotides = nucleotides + [nuc]
	nuc = raw_input('Enter the nucleotide sequence: ')


sequences = []

for seq in nucleotides:
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
			nuc1 = nuc1 + '*'
	sequences = sequences + [nuc1]

list1 = []
for x in sequences:
	a = x.count('a') + x.count('A')
	t = x.count('t') + x.count('T')
	g = x.count('g') + x.count('G')
	c = x.count('c') + x.count('C')
	char = x.count('*')
	list1 = list1 + [(a,t,g,c,char)]

