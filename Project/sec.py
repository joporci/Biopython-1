file_name = '3AYU.pdb'
pdb_file = open('test.pdb', 'r')
option = 'S'
aaA = ''
aaB = ''
helix = []
sheet = []
for line in pdb_file:
	if 'SEQRES' in line:
		chain = line[11]
		if chain == 'A':
			aaA = aaA + line[19:].rstrip() + ' '
		else:
			aaB = aaB + line[19:].rstrip() + ' '

	if 'HELIX' in line:
		helix_id = line[9]
		sub = line[13]
		chain = line[19]
		pos_a = line[22:26].strip(' ')
		pos_a = int(pos_a)
		pos_b = line[34:37].strip(' ')
		pos_b = int(pos_b)
		helix = helix + [(chain,helix_id,sub, pos_a, pos_b)]
	if 'SHEET' in line:
		chain = line[21]
		sheet_id = line[9] + line[13]
		sub = line[13]
		pos_a = line[23:26].strip(' ')
		pos_a = int(pos_a)
		pos_b = line[34:37].strip(' ')
		pos_b = int(pos_b)
		sheet = sheet + [(chain,sheet_id, sub, pos_a, pos_b)]
aaA = aaA.split(' ')
aaB = aaB.split(' ')

aaB = aaB[0:-1]
aaA = aaA[0:-1]


table = {
    'A': ('ALA'),
    'C': ('CYS'),
    'D': ('ASP'),
    'E': ('GLU'),
    'F': ('PHE'),
    'G': ('GLY'),
    'I': ('ILE'),
    'H': ('HIS'),
    'K': ('LYS'),
    'L': ('LEU'),
    'M': ('MET'),
    'N': ('ASN'),
    'P': ('PRO'),
    'Q': ('GLN'),
    'R': ('ARG'),
    'S': ('SER'),
    'T': ('THR'),
    'V': ('VAL'),
    'W': ('TRP'),
    'Y': ('TYR'),
}

dataA = ''
dataB = ''
for aa in aaA:
	for a in table:
		if aa in table[a]:
			dataA = dataA + a

for aa in aaB:
	for a in table:
		if aa in table[a]:
			dataB = dataB + a


charA = '-'*len(dataA)
charB = '-'*len(dataB)
for a in sheet:
	if a[0] == 'A':
		charA = charA[:a[3]-1] + '|'*(a[4]+1-a[3]) + charA[(a[4]):]
	if a[0] == 'B':
		charB = charB[:a[3]-1] + '|'*(a[4]+1-a[3]) + charB[(a[4]):]
for b in helix:
	if b[0] == 'A':
		charA = charA[:b[3]-1] + '/'*(b[4]+1-b[3]) + charA[(b[4]):]
	if b[0] == 'B':
		charB = charB[:b[3]-1] + '/'*(b[4]+1-b[3]) + charB[(b[4]):]

sec_idA = ' '*len(dataA)
sec_idB = ' '*len(dataB)
for a in sheet:
	if a[0] == 'A':
		sec_idA = sec_idA[:a[3]-1] + a[1] + sec_idA[a[3]+1:]
	if a[0] == 'B':
		sec_idB = sec_idB[:a[3]-1] + a[1] + sec_idB[a[3]+1:]
for a in helix:
	if a[0] == 'A':
		sec_idA = sec_idA[:a[3]-1] + a[1] + sec_idA[(a[3]):]
	if a[0] == 'B':
		sec_idB = sec_idB[:a[3]-1] + a[1] + sec_idB[(a[3]):]

print 'Chain A:','\b\n', '(1)'
a = 0
for i in range(1, len(dataA)):
	if i % 80 == 0:
		print dataA[a:i], '\b\n', charA[a:i], '\b\n', sec_idA[a:i]
		a = i
		
print dataA[a:], '\b\n', charA[a:], '\b\n', sec_idA[a:], '\b\n', '(',len(dataA),'\b)' '\n' 	




print 'Chain B:','\b\n', '(1)'
b = 0
for i in range(1, len(dataB)):
	if i % 80 == 0:
		print dataB[b:i], '\b\n', charB[b:i], '\b\n', sec_idB[b:i]
		a = i
		
print dataB[b:], '\b\n', charB[b:], '\b\n', sec_idB[b:], '\b\n', '(',len(dataB),'\b)' '\n'






