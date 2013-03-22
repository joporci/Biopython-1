# Now replace each Thymine('t') for an Uracil('u'), and write a new fasta file with the result.

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
		
A = string2.count('A')
T = string2.count('T')
C = string2.count('C')
G = string2.count('G')

print "A is",A, 'T is',T,'C is', C, 'G is',G

import textwrap	
new_fasta = textwrap.fill(string2, 50)

new_fasta = new_fasta.replace('T', 'u')

new_fastafile = open('new_fasta.txt', 'w+')
new_fastafile.write('>sequence 2\n')
new_fastafile.write(new_fasta)
new_fastafile.close()

