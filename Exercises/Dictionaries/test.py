s="fuy giuygiuu uguihg iug ui i iugiu huh iu u g ug uig uigg iug igiug iugiug igiug uig uig uig iu ugiugiugyfiygiygiyyhgiy iy iyg i ittttttttttttttttttttttttttt nnnnnn rrrrrrrr ttttttttttttttt fdddddddddddddd nnnnnnnnnn aaaaaaaaaaaa sssssssssssss rrrrrrr"
x = []
y = 0
if len(s) > 60:
	for a in range(len(s)):
		if (a) % 60 == 0:
			if a != 0:
				value =  s[:a].rindex(' ')
				x = x + [value]
b = 0
for a in x:
	print s[b:a]
	b = a
print s[b:]

