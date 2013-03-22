file_name = '3AYU.pdb'
file_loaded = True
pdb_file = open('test.pdb', 'r')
option = 'M'
if option == 'M':
	if file_loaded ==True:
		aaA = ''
		aaB = ''
		for line in pdb_file:
			if 'SEQRES' in line:
				num = line[14:17]
				chain = line[11]
				if chain == 'A':
					aaA = aaA + line[19:].rstrip() + ' '
				else:
					aaB = aaB + line[19:].rstrip() + ' '
		aaB = aaB[0:-1].split(' ')
		aaA = aaA[0:-1].split(' ')
		pdb_file.seek(0)
		helix_class = {1:'Right-handed alpha (default)', 2:'Right-handed omega', 3:'Right-handed pi', 4:'Right-handed gamma', 5:'Right-handed 3 - 10', 6:'Left-handed alpha', 7:'Left-handed omega', 8:'Left-handed gamma', 9:'2 - 7 ribbon/helix', 10:'Polyproline'}
		print 'Choose one of the Manipulation Options:\n', 'List (L)    Edit (E)    New (N)    Remove (R)    Main Menu (M)\n'
		manipulation = ''
		while manipulation != 'M':

			manipulation = raw_input(': ').upper()
			if manipulation == 'L':
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
					
			if manipulation == 'E':
				ask_sec_struc = raw_input('Do you want to edit Helix (H) or Sheet (S) : ').upper()
				if ask_sec_struc == "H":
					ask_helix = raw_input('Which helix do you want to edit (1-3): ')
					
					for line in pdb_file:
						if 'HELIX' in line:
							if ask_helix == line[13].strip():
								new_line = line
								change1 = raw_input('Chain '+'['+line[19]+']: ').upper()
								change2 = raw_input('initSeqNum '+'['+line[22:25].strip()+']: ')
								print 'That position corresponds to the amino acid ' + aaA[int(change2)-1]
								change3 = raw_input('endSeqNum'+'['+line[33:37].strip()+']: ')
								print 'That position corresponds to the amino acid ' + aaA[int(change3)-1]
								change4 = raw_input('helixClass: ')
								if int(change4) in helix_class.keys():
									print helix_class[int(change4)]
								change5 = raw_input('comment: ')
								new_line = new_line[:15]+aaA[int(change2)-1]+new_line[18]+change1+new_line[20:21]+change2+ ' '*(3-len(change2))+new_line[25:26]+aaA[int(change3)-1]+new_line[30:34]+change3+' '*(3-len(change3))+new_line[37:39]+change4+change5+ ' '*(29-len(change5))+new_line[69:]
					
					pdb_file.seek(0)
					print 'The Helix '+ask_helix+' has been successfully edited.'	

				if ask_sec_struc == "S":
					ask_sheet = raw_input('Which helix do you want to edit (1A-2A), (1B-6B), (1C-2C): ')
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
								else:
									print 'That position corresponds to the amino acid ' + aaB[int(change3)-1]
					pdb_file.seek(0)			
					print 'The Sheet '+ask_sheet+' has been successfully edited.'



			if manipulation == 'N':
				new_line = ' '*80
				add = raw_input('Do you want to add Helix (H) or Sheet (S): ').upper()
				if add == 'H':
					chain = raw_input('Chain: ').upper()
					initSeqNum  = raw_input('initSeqNum:')
					print 'This position corresponds to the amino acid ' + aaA[int(initSeqNum)]
					endSeqNum  = raw_input('endSeqNum:')
					print 'This position corresponds to the amino acid ' + aaA[int(endSeqNum)]
					helixClass = raw_input('helixClass: ')
					if int(helixClass) in helix_class.keys():
						print helix_class[int(helixClass)]
					comment = raw_input('comment: ')
					print 'The helix '+' has been successfully created.'
					new_line = 'HELIX '+ ' '+'num'+' '+'id '+' '+'irn'+' '+'C'+' '+'isn '+'C'+' '+'ern'+' '+'E'+' '+'esn '+'C'+'HC'+'comment                      '+'length'
				if add == 'S':
					chain = raw_input('Chain: ').upper()
					initSeqNum  = raw_input('initSeqNum:')
					if chain == 'A':
						print 'This position corresponds to the amino acid ' + aaA[int(initSeqNum)]
					else:
						print 'This position corresponds to the amino acid ' + aaB[int(initSeqNum)]
					endSeqNum  = raw_input('endSeqNum:')
					if chain == 'A':
						print 'This position corresponds to the amino acid ' + aaA[int(endSeqNum)]
					else:
						print 'This position corresponds to the amino acid ' + aaB[int(endSeqNum)]
					print 'The sheet '+' has been successfully created.'



			if manipulation == 'R':
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

		
print new_line
