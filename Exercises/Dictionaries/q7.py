
dic = {
"Hitchhiker's Guide to the Galaxy": 1,
"The Restaurant at the End of the Universe": 2,
"Life, the Universe, and Everything": 3,
"So Long, and Thanks for all the Fish!": 4,
"Mostly Harmless": 5
}

#3. This program starts by declaring the above dictionary as a literal, and outputs the books in order.

dic2 = {}

for k in dic:
	dic2[dic[k]] = k

print dic2





#4 This program starts by declaring the above dictionary as a literal, and then asks the user for a number, and prints out name of the book which has the given number.

number = int(raw_input('Enter number: '))

for k in dic:
	if dic[k] == number:
		print k




#5 The algorithm starts by declaring the above dictionary as a literal, then proceeds to switch the keys and values, so that values become keys, and vice versa. Print out the resulting dictionary

dic1 = {}

for k in dic:
	dic1[dic[k]] = k


print dic1


