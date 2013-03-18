# This program receive as many sequences as the user wants and calculates the GC ratio of each sequence. It should displays the sequences in order of its GC ratio, with the G's and C's in upper case and the T's and A's in lower case and in front of the sequence the calculated GC ratio. Finally it should show was the avarage GC ration among all the sequences.



nuc = raw_input('Enter the nucleotide sequence: ')	# This allows the user to enter a sequence of choice
sequences = []					# An empty list that will be used to store the sequences


while nuc != '':					# The loop allows to enter as many sequences as desired
	sequences = sequences + [nuc]		# the nucleotide sequence is enclosed in brackets so it can be added in the 
	nuc = raw_input('Enter the nucleotide sequence: ')


print '\n',				# This is to print a blank line for a better view of the output display


nucleotides = []
for seq in sequences:				# This loop is there to replace bases
	if 'g' in seq:
		new_seq = seq.replace('g', 'G')	# lower case g replaced by upper case G in all sequences and saved in new_seq
	else:
		new_seq = seq			# defining new_seq incase there is no g in the sequence
	if 'c' in new_seq:
		new_seq = new_seq.replace('c', 'C')	# lower case c replaced by upper case C in all sequences and saved in new_seq
	if 'T' in new_seq:
		new_seq = new_seq.replace('T', 't')	# upper case T replaced by lower case t in all sequences and saved in new_seq
	if 'A' in new_seq:
		new_seq = new_seq.replace('A', 'a')	# upper case A replaced by lower case a in all sequences and saved in new_seq
	nucleotides = nucleotides + [new_seq]


gc_list = []
for a in nucleotides:			# This loop calculates the GC-ratio of each sequence
	GC = a.count('G') + a.count('C')# counting the number of G and C bases in the sequence
	seq_length = float(len(a))	# converting the length of the sequence into a float point
	GC_ratio = GC/seq_length	# calculationg the GC ration by diving total number of G's and C's by the total number of bases ib sequence
	gc_list = gc_list + [[a, GC_ratio]]# Storing the GC ratio together with its sequence in a list

ratio_list = sorted(gc_list, key=lambda a: a[1])# sorting the gc_ratio list in-order of increasing ratio

for i in ratio_list:			# Displaying the output of the sorted list
	print i[0], '%.4f' % i[1]	# printing to 4 decimal places

print '\n',				# This is to print a blank line for a better view of the output display


# Calculating the overal ration in the whole genome
total = 0				# the starting total of the number of bases		
number = len(ratio_list)		# the number of sequences in the entire genome
for a in ratio_list:			# loop over each sequence
		total = total + a[1]	# the total becomes previous total plus the Gc ratio of the sequence in the loop

overal_GC_ratio = total/number		# the overal ratio is calculated by dividing the total of the GC ratios by the number of sequences

print 'The overal GC ratio is %.4f' % overal_GC_ratio # displays the output of the GC_ratio in 4 decimal places

	

	
