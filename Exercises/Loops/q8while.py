# this program requires a DNA sequence input and put the sequence in lower case

def lowerbase(seq): # Create a function that checks the contents of the sequence
	if seq == 'g' or seq == 'G':
		return 'g'
	elif seq == 'a' or seq == 'A':
		return 'a'
	elif seq == 't' or seq == 'T':
		return 't'
	else:
		return 'c'

result = "" # create a variable that will store the result of the function
sequence = raw_input('Enter sequence: ')
counter = 0
while counter < len(sequence):
	result = result + lowerbase(sequence[counter])
	counter = counter +1

print result

