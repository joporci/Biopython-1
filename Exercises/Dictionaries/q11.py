# Extend your solution to the previous problem, by allowing customers to enter multi-line comments, and to terminate their comments by entering a blank line. If the comment is entirely blank, i.e. the first line is blank, then it does not overwrite the former comment if any. Also, ensure that when the comments are outputted back, either because of the 'showcomments' command, or a repeat customer entering their name, that the line width of the outputted comments does not exceed 60 characters, nor break a word in two, i.e. lines are only broken on white space.

name = raw_input('Enter name: ')
comment = raw_input('Enter comment: ')

comments = ''
while comment != '':
	comments = comments + ' ' + comment
	comment = raw_input('Enter comment: ')

guest_book = {}

while name != 'quit':
	comment = comments
	guest_book[name] = comment
	name = raw_input('Enter name or "type quit to exit the program"  ')
	if name != 'quit':
		comment = '.'
		comments = ''
		while comment != '':
			comments = comments + ' ' + comment
			if name in guest_book.keys():
				print 'user already in'
				write = raw_input('Do you want to enter new comment? if yes type yes or just hit enter if no ')
				if write == 'yes':
					comment = raw_input('Enter comment: ')
				else:
					if write == '':
						break
				
			else:
				comment = raw_input('Enter comment: ')
	
	

for name in guest_book:
	print "These are the comments for", name
	
	x = []
	y = 0

	if len(guest_book[name]) > 60:
		for a in range(len(guest_book[name])):
			if (a) % 60 == 0:
				if a != 0:
					value =  guest_book[name][:a].rindex(' ')
					x = x + [value]
			
				
					b = 0
					for a in x:
						print guest_book[name][b:a]
						b = a
						print guest_book[name][b:]
			

	else:
		print guest_book[name]


