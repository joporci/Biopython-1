# Analysis of a PDB file
# Author: Faya Ngonidzashe
# 18 March 2013

option = '' # This variable is assigned an empty string so the while loop will have a starter
file_name = None	# There is no file name at start therefore None
file_loaded = False	# No file is loaded so the variable has a value of False


# This loop, repeats a menu that has several operation and the loop can be cut when the user put a quit option in the menu
# The  print command in the loop, displays an output of the main menu
while option != 'Q':
	print '*'*80,'\b\n', '* PDB FILE ANALYSER', '*'.rjust(60), '\b\n', '*'*80,'\b\n', '* Select an option from below:', '*'.rjust(49), '\b\n', '*','*'.rjust(78),'\b\n', '*\t1) Open a PDB File', '(O)'.rjust(20), '*'.rjust(32), '\b\n', '*\t2) Information', '(I)'.rjust(24), '*'.rjust(32), '\b\n', '*\t3) Show histogram of amino acids', '(H)'.rjust(6), '*'.rjust(32), '\b\n', '*\t4) Display secondary structure', '(S)'.rjust(8), '*'.rjust(32), '\b\n', '*\t5) Manipulate helix or sheet', '(M)'.rjust(10), '*'.rjust(32), '\b\n', '*\t6) Export PDB file', '(X)'.rjust(20), '*'.rjust(32), '\b\n', '*\t7) Exit', '(Q)'.rjust(31), '*'.rjust(32), '\b\n', '*', '*'.rjust(78), '\b\n', '*', 'Current PDB:'.rjust(70),file_name, '*'.rjust(2), '\b\n','*'*80,'\b\n',  


	option = raw_input(': ').upper()	# The option allows the user to pick any option to run from the main menu

##########################################################################################################################################
# This part of the program allows the user to open a file and all the other sections are dependent on this section except the quit option#
##########################################################################################################################################
	if option == 'O':			# Check if the option typed by the user is O

		while file_loaded!= True:	# If true, then enters into a loop that only exit when a file is loaded
			file_name = raw_input('Enter a Valid Path for a PDB File: ')# allows the user to enter a path for the file
			import os.path		# importing the os module to check the paths in the system
			file_loaded = os.path.exists(file_name) # a variable given boolean value to test whether a path exist
			if file_loaded == True:			# check whether the  path exist
				pdb_file = open(file_name, 'r') # if path exist the pdfile is opened for reading and given a variable
				print 'The File', file_name, 'has been successfully loaded' 
			else:
				print 'Error, the file does not exist'

			aaA = '' # a variable that will be given a vulue of a string of amino acids in chainA
			aaB = '' # a variable that will be given a vulue of a string of amino acids in chainB
			helix = []# a list that will be used to store all the helices in the protein
			sheet = [] # a list that will be used to store all the sheets in the protein
			for line in pdb_file: # the loop will pick up and store all the amino acids, helices and sheets in the protein
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
			pdb_file.seek(0)

			# this dictionary has the amino acids one letter reference to its name
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

			dataA = '' # this empty string will store all the amino acids in the chain A using one letter code
			dataB = '' # this empty string will store all the amino acids in the chain B using one letter code
# this loop does the changes of the 3letter to one letter one way of defining amino acids in chain A
			for aa in aaA:
				for a in table:
					if aa in table[a]:
						dataA = dataA + a
# this loop does the changes of the 3letter to one letter one way of defining amino acids in chain A
			for aa in aaB:
				for a in table:
					if aa in table[a]:
						dataB = dataB + a
		

##################################################################################################			
# This part of the program deals with displaying the information of the protein from the PDB file#
##################################################################################################		
	if option == 'I':			
		if file_loaded ==True:
			Title = ''
			Chains = []
			aa_number = [] # to store the number of amino acids in the protein
			HA = 0 # helices in chain A so far
			HB = 0 # helices in chain B so far
			SA = 0 # sheets in chain A so far
			SB = 0 # sheets in chain B so far
# this loop checks for the title, chains in the protein, amino acids and secondary structures and store them
			for line in pdb_file:
				if 'TITLE' in line:
					Title = Title + line[10:].strip()
				if 'DBREF' in line:
					char = line[12]
					if char in Chains:
						Chains = Chains
					else:
						Chains = Chains + [char]
				if 'SEQRES' in line:
					num = line[14:17]
					if num in aa_number:
						aa_number = aa_number
					else:
						aa_number = aa_number + [num]
	
		
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




					
			import textwrap		
		
			print 'PDB File:', file_name, '\b\n', 'Title:',Title,'\b\n', 'CHAINS: %s and %s' % (Chains[0], Chains[1]), '\b\n', ' - Chain', Chains[0],'\b\n', '     Number of amino acids:    %s' % aa_number[0], '\n     Number of helix:            %s' % HA, '\n', '     Number of sheet:            %s' % SA, '\b\n', '     Sequence: ',textwrap.fill(dataA,50).replace("\n","\n                "),'\b\n'' - Chain', Chains[1],'\b\n', '     Number of amino acids:    %s' % aa_number[1], '\n     Number of helix:            %s' % HB, '\n', '     Number of sheet:            %s' % SB, '\b\n', '     Sequence:', dataB, '\b\n',

			pdb_file.seek(0)
		else:
			print 'No file is loaded, use option O first!!!'




######################################################################################################################
# This part of the program deals with displaying the amino acids of the protein from the PDB file through a histogram#
######################################################################################################################
	if option == 'H':
		if file_loaded ==True:
			
			aa = aaA + aaB # addition of all the amino acids in the chains

# this function stores the amino acid and its total number of occurance in a dictionary and returns the dictionary
			def histogram(his):
			    store_aa = {}
			    for x in his:
				if x in store_aa:
				    store_aa[x] += 1
				else:
				    store_aa[x] = 1
			    return store_aa

			his_aa = histogram(aa) # a dictionary with the amino acids as key and the total as the value
			his_aa = his_aa.items() # list containing tuples of all key:value pairs in the dictionary
# this print command gives the user an option to choose what to sort using
			print 'Choose an option to order by: ', '\b\n', '   number of amino acids - ascending (an)', '\b\n', '   number of amino acids - descending (dn)', '\b\n', '   alphabetically - ascending        (aa)', '\b\n', '   alphabetically - descending       (da)', '\b\n',

			order = raw_input('order by: ').lower() # allows the user to put the sorting method
# depending with what the user inputs the histogram is displayed in that way
			if order == 'aa':
				alp_asc = sorted(his_aa, key=lambda a: a[0])
				for item in alp_asc:
					print item[0], '(', item[1],'\b)', ':', '*'*(item[1])

			if order == 'da':
				alp_dsc = sorted(his_aa, key=lambda a: a[0])
				alp_dsc = alp_dsc[::-1]
				for item in alp_dsc:
					print item[0], '(', item[1],'\b)', ':', '*'*(item[1])

			if order == 'an':
				num_asc = sorted(his_aa, key=lambda a: a[1])
				for item in num_asc:
					print item[0], '(', item[1],'\b)', ':', '*'*(item[1])

			if order == 'dn':
				num_dsc = sorted(his_aa, key=lambda a: a[1])
				num_dsc = num_dsc[::-1]
				for item in num_dsc:
					print item[0], '(', item[1],'\b)', ':', '*'*(item[1])
		
	
			pdb_file.seek(0)
		else:
				print 'No file is loaded, use option O first!!!'

#####################################################################################################################################
# This part of the program deals with displaying the secondary structure of the protein from the PDB file through special characters#
#####################################################################################################################################
	if option == 'S':
		if file_loaded ==True:
			# the special characters that will be used to represent amino acids not in a sec structure (-), helix (/), sheet (|)
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

			# the identities of each secondary structure in the protein will be represented
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

# the amino acids, special chracters and the identities will be displayed and only 80 characters are allowed per line
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
			pdb_file.seek(0)
		else:
			print 'No file is loaded, use option O first!!!'



#####################################################################################################################################
# This part of the program deals with manipulating the secondary structure of the protein from the PDB file through various options #
#####################################################################################################################################	
	if option == 'M':
		if file_loaded ==True:
# helix class is a dictionary that shows the key as the number or id of class and the value as the type represented by the number
			helix_class = {1:'Right-handed alpha (default)', 2:'Right-handed omega', 3:'Right-handed pi', 4:'Right-handed gamma', 5:'Right-handed 3 - 10', 6:'Left-handed alpha', 7:'Left-handed omega', 8:'Left-handed gamma', 9:'2 - 7 ribbon/helix', 10:'Polyproline'}
			
			manipulation = ''
# this loop allows the user to execute various manipulation methods
			while manipulation != 'M':
				print 'Choose one of the Manipulation Options:\n', 'List (L)    Edit (E)    New (N)    Remove (R)    Main Menu (M)\n'
				manipulation = raw_input(': ').upper()# allows the user to choose what to do
			
				if manipulation == 'L': # option choosen is to list
					ask = raw_input('Do you want to list the Helix (H) or Sheet (S) : ').upper()
					if ask == "H":
						a = 1
						for line in pdb_file:
							if 'HELIX' in line:
								helix_cl = helix_class[int(line[38:40].strip())]
								print 'Helix', a, 'of', '\n', ' serNum:', line[9].rjust(7), '\n', '  helixID:', line[13].rjust(5), '\n', '  initResName:', line[15:18].rjust(1), '\n', '  initChainID:', line[19].rjust(1), '\n', '  initSeqNum:', line[22:25].rjust(4), '\n', '  initICode:', line[25].rjust(4), '\n', '  endResName:', line[27:30].rjust(4), '\n', '  endChainID:', line[31].rjust(2), '\n', '  endSeqNum:', line[33:37].rjust(5), '\n', '  endICode:', line[37].rjust(5), '\n', '  helixClass:', helix_cl.rjust(3), '\n', '  comment:', line[40:70].rjust(6), '\n', '  length:', line[71:76].rjust(7), '\n',
								a = a+1
						pdb_file.seek(0)

					if ask == 'S':
						a = 1
						for line in pdb_file:
							if 'SHEET' in line:
								print 'Sheet', a, 'of', '\n', '  strand:', line[7:10].rjust(6), '\n', '  sheetID:', line[11:14].rjust(5), '\n','  numStrands:', line[14:16].rjust(1), '\n','  initResName:', line[17:20].rjust(1), '\n', '  initChainID:', line[21].rjust(1), '\n', '  initSeqNum:', line[22:26].strip().rjust(3), '\n', '  initICode:', line[26].rjust(4), '\n', '  endResName:', line[28:31].rjust(4), '\n', '  endChainID:', line[32].rjust(2), '\n', '  endSeqNum:', line[33:37].strip().rjust(5), '\n', '  endICode:', line[37].rjust(5), '\n', '  sense:', line[38:40].rjust(7), '\n', '  curAtom:', line[41:45].rjust(7), '\n', '  curResname:', line[45:48].rjust(4), '\n', '  curChainID:', line[49].rjust(2), '\n', '  curResseq:', line[50:54].strip().rjust(5), '\n', '  curICode:', line[54].rjust(7), '\n', '  prevAtom:', line[56:60].strip().rjust(4), '\n', '  prevResName:', line[60:63].rjust(2), '\n', '  prevChainID:', line[64].rjust(1), '\n', '  prevResSeq:', line[65:69].strip().rjust(3), '\n', '  prevICode:', line[69].rjust(4), '\n',
								a = a+1
						pdb_file.seek(0)
					
				if manipulation == 'E': # option chosen is to edit the secondary structure of choice
					ask_sec_struc = raw_input('Do you want to edit Helix (H) or Sheet (S) : ').upper()
					if ask_sec_struc == "H":
						ask_helix = raw_input('Which helix do you want to edit (1-3): ')
						for line in pdb_file:
							if 'HELIX' in line:
								if ask_helix == line[13].strip():
									change1 = raw_input('Chain '+'['+line[19]+']: ').upper()
									change2 = raw_input('initSeqNum '+'['+line[22:25].strip()+']: ')
									print 'That position corresponds to the amino acid ' + aaA[int(change2)-1]
									change3 = raw_input('endSeqNum'+'['+line[33:37].strip()+']: ')
									print 'That position corresponds to the amino acid ' + aaA[int(change3)-1]
									change4 = raw_input('helixClass: ')
									if int(change4) in helix_class.keys():
										print helix_class[int(change4)]
									change5 = raw_input('comment: ')
									helix[(int(ask_helix)-1)]=(change1,ask_helix,line[13], int(change2),int(change3))
									
						pdb_file.seek(0)
						print 'The Helix '+ask_helix+' has been successfully edited.'	

					if ask_sec_struc == "S":
						ask_sheet = raw_input('Which helix do you want to edit (1A-2A), (1B-6B), (1C-2C): ')
						dic = {'1A':1,'2A':2,'1B':3,'2B':4,'3B':5,'4B':6,'5B':7,'6B':8,'1C':9,'2C':10}
						for line in pdb_file:
							if 'SHEET' in line:
								if ask_sheet == line[9]+line[13].strip():
									change1 = raw_input('Chain '+'['+line[21]+']: ').upper()
									change2 = raw_input('initSeqNum '+'['+line[22:26].strip()+']: ')
									if change1 == 'A':
										print 'That position corresponds to the amino acid ' + aaA[int(change2)-1]
									else:
										print 'That position corresponds to the amino acid ' + aaB[int(change2)-1]
									change3 = raw_input('endSeqNum'+'['+line[33:37].strip()+']: ')
									if change1 == 'A':
										print 'That position corresponds to the amino acid ' + aaA[int(change3)-1]
										sheet[(dic[ask_sheet]-1)] = (change1,ask_sheet,line[13], int(change2),int(change3))
									
									else:
										print 'That position corresponds to the amino acid ' + aaB[int(change3)-1]
										sheet[(dic[ask_sheet]-1)] = (change1,ask_sheet,line[13],int(change2),int(change3))
						pdb_file.seek(0)			
						print 'The Sheet '+ask_sheet+' has been successfully edited.'



				if manipulation == 'N': # option chosen is to create a new secondary structure
					add = raw_input('Do you want to add Helix (H) or Sheet (S): ').upper()
					if add == 'H':
						chain = raw_input('Chain: ').upper()
						helix_id = raw_input('Sheet-id (number>3): ')
						sub_structure = raw_input('sub (number>3): ').upper()
						initSeqNum  = raw_input('initSeqNum:')
						print 'This position corresponds to the amino acid ' + aaA[int(initSeqNum)]
						endSeqNum  = raw_input('endSeqNum:')
						print 'This position corresponds to the amino acid ' + aaA[int(endSeqNum)]
						helixClass = raw_input('helixClass: ')
						if int(helixClass) in helix_class.keys():
							print helix_class[int(helixClass)]
						comment = raw_input('comment: ')
						helix = helix + [(chain,helix_id,sub_structure, int(initSeqNum), int(endSeqNum))]
					
					if add == 'S':
						dic = {'1A':1,'2A':2,'1B':3,'2B':4,'3B':5,'4B':6,'5B':7,'6B':8,'1C':9,'2C':10}
						chain = raw_input('Chain: ').upper()
						sheet_id = raw_input('Sheet-id A(>2),B(>6),C(>2): ')
						sub_structure = raw_input('sub (alphabet): ').upper()
						initSeqNum  = raw_input('initSeqNum:')
						total = int(raw_input('Total number of sheets now: '))
						sh_id = sheet_id+sub_structure
						if chain == 'A':
							print 'This position corresponds to the amino acid ' + aaA[int(initSeqNum)]
						else:
							print 'This position corresponds to the amino acid ' + aaB[int(initSeqNum)]
						endSeqNum  = raw_input('endSeqNum:')
						if chain == 'A':
							print 'This position corresponds to the amino acid ' + aaA[int(endSeqNum)]
							sheet = sheet + [(chain,sh_id,sub_structure, int(initSeqNum), int(endSeqNum))]
						else:
							print 'This position corresponds to the amino acid ' + aaB[int(endSeqNum)]
							sheet = sheet + [(chain,sh_id,sub_structure, int(initSeqNum), int(endSeqNum))]
							dic[sheet_id+sub_structure] = total
						print 'The sheet '+' has been successfully created.'
					


				if manipulation == 'R': # option is to remove a secondary structure
					ask = raw_input('Do you want to remove Helix (H) or a Sheet (S): ').upper()
					if ask == 'H':
						ask_again = raw_input('Which Helix do you want to remove (1-4):')
						print 'Are you sure you want to delete the helix?'
						for line in pdb_file:
							if 'HELIX' in line:
								if ask_again == line[9]:
									print line,
						confirm = raw_input('Y/N? ').upper()
						if confirm == 'Y':
							print 'The Helix '+ask_again+' has been successfully removed.'
						else:
							print 'The helix could not be deleted due to lack of confirmation'
					if ask == 'S':
						ask_again = raw_input('Which Sheet do you want to remove (1A-2A), (1B-6B), (1C-2C):')
						print 'Are you sure you want to delete the sheet?'
						for line in pdb_file:
							if 'SHEET' in line:
								if ask_again == line[9]+line[13].strip():
									print line,
						confirm = raw_input('Y/N? ').upper()
						if confirm == 'Y':
							print 'The Sheet '+ask_again+' has been successfully removed.'
						else:
							print 'The sheet could not be deleted due to lack of confirmation'
	
				

		else:
			print 'No file is loaded, use option O first!!!'

#new_line = new_line[:15]+aaA[int(change2)-1]+new_line[18]+change1+new_line[20:21]+change2+ ' '*(3-len(change2))+new_line[25:26]+aaA[int(change3)-1]+new_line[30:34]+change3+' '*(3-len(change3))+new_line[37:39]+change4+change5+ ' '*(29-len(change5))+new_line[69:]
									#temp_file.write(new_line)
	#							else:
	#								temp_file.write(line)


