# Modify q1.py progam to print the name of the sequence(first line of a fasta file, starting for '>'), then print the total of nucleotides in the sequence and now print the nucleotides but each line should have 50 characters

sequence = open('./fasta.txt', 'r')
print "The name of the sequence is", sequence.readline()

total = 0
for line in sequence:
	total = total + (line.count('A') + line.count('C') + line.count('T') + line.count('G'))
print 'The total number of nucleotides is', total

print '\n'

sequence.close()
f = open('./fasta.txt', 'r')
f.readline()

list1 = []

for nuc in f:
	list1.append(nuc)
	
string1 = ''.join(list1)
string2 = string1.replace('\n', '')


import textwrap			
print textwrap.fill(string2, 50)
f.close()

# Gustavo 50 characters
# def func(seq, numberperline, identation=0)
	#seq1 = ''
	# index= 0
	#whhile index <= len(seq):
		#seq1 += 
	#while index 
	
		
	

		
