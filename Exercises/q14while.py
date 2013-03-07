phrase1 = raw_input('Enter phrase: ')
phrase2 = raw_input('Enter phrase: ')
letter = raw_input('Enter single letter: ')
count = 0
a = 0
b = 0
while count < len(phrase1):
	first = phrase1[count]
	if letter == first:
		a = a + 1
	count = count + 1
print a

count = 0

while count < len(phrase2):
	second = phrase2[count]
	if letter == second:
		b = b + 1
	count = count + 1
print b

if a > b:
	print phrase1, "has the most occurances of the input letter", letter
else:
	print phrase2, "has the most occurances of the input letter", letter
