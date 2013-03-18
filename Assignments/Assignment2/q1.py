# With the following list of nucleotide sequences, the program create a list of tuples where each tuple contains the number of A,T,G and C. (case insensitive)

nucleotides = [							# The given list with the list-name nucleotides
	"tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
	"tttgggta",
	"tgactgtagcagtcaTATCGATG",
	"TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
	"ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]

list1 = []				# list1 is an empty list that is going to be used to store the count of each base
for x in nucleotides:			# The loop repeats each sequence in the nucleotide sequence
	a = x.count('a') + x.count('A')	# a is a variable that has the value of sum of both lower and upper-case a
	t = x.count('t') + x.count('T')	# t is a variable that has the value of sum of both lower and upper-case t
	g = x.count('g') + x.count('G')	# g is a variable that has the value of sum of both lower and upper-case g
	c = x.count('c') + x.count('C')	# c is a variable that has the value of sum of both lower and upper-case c
	list1 = list1 + [(a,t,g,c)]	# list1 is will b the list of the counts of the bases in each sequence saved in a tuple
	
print list1
	
