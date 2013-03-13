# A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner.

name = raw_input('Enter name: ').lower()
comment = raw_input('Enter comment: ')

guest_book = {}


while name != 'quit':
	guest_book[name] = comment
	name = raw_input('Enter name or "type quit to exit the program"  ').lower
	if name != 'quit':
		if name in guest_book.keys():
			print guest_book[name]
			write = raw_input('Enter new comment or just press enter if no comment')
			if write == '':
				comment = guest_book[name]
			else:
				comment = write
		else:
			comment = raw_input('Enter comment: ')
	
	
print guest_book
