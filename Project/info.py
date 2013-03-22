# Information data

file_name = '3AYU.pdb'
test = open('test.pdb', 'r')


Title = ''
Chains = []
aa_number = []
helix = []
aaA = ''
aaB = ''
HA = 0
HB = 0
SA = 0
SB = 0
for line in test:
	if 'TITLE' in line:
		Title = Title + line[10:].rstrip('\n') + '\b'
	if 'DBREF' in line:
		char = line[12]
		if char in Chains:
			Chains = Chains
		else:
			Chains = Chains + [char]
	if 'SEQRES' in line:
		num = line[14:17]
		chain = line[11]
		if num in aa_number:
			aa_number = aa_number
		else:
			aa_number = aa_number + [num]
		if chain == 'A':
			aaA = aaA + line[19:].rstrip() + ' '
		else:
			aaB = aaB + line[19:].rstrip() + ' '
		
	if 'HELIX' in line:
		ch = line[19]
		if ch == 'A':
			HA = HA + 1
		if ch == 'B':
			HB = HB + 1
	if 'SHEET' in line:
		ch = line[21]
		if ch == 'A':
			SA = SA + 1
		if ch == 'B':	
			SB = SB + 1

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


		
import textwrap		
		
print 'PDB File:', file_name, '\b\n', 'Title:',Title,'\b\n', 'CHAINS: %s and %s' % (Chains[0], Chains[1]), '\b\n', ' - Chain', Chains[0],'\b\n', '     Number of amino acids:    %s' % aa_number[0], '\n     Number of helix:            %s' % HA, '\n', '     Number of sheet:            %s' % SA, '\b\n', '     Sequence: ',textwrap.fill(dataA,50).replace("\n","\n                "),'\b\n'' - Chain', Chains[1],'\b\n', '     Number of amino acids:    %s' % aa_number[1], '\n     Number of helix:            %s' % HB, '\n', '     Number of sheet:            %s' % SB, '\b\n', '     Sequence:', dataB, '\b\n',

