# Add to q2 program the capability of counting how many times each nucleotide appears.

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
		
A = string2.count('A')
T = string2.count('T')
C = string2.count('C')
G = string2.count('G')

print "A is",A, 'T is',T,'C is', C, 'G is',G
