# The program receives the name of a fasta file(use this file as an example) from the command line, and print the content of the file.

import sys

path = sys.argv[1]

f = open(path, 'r')
for seq in f:
	print seq.rstrip()

#Gustavo's method
# f = open('./fasta.txt', 'r')
# seq = f.read()
#print seq
