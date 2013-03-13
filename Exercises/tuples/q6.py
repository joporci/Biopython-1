# Given a list of tuples each specifying a subject name and a grade symbol ('A' - 'F') in the form [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]: 

sub_grade = [('Maths', 'D'), ('CompSci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

# The first algorithm prints out the subject with the highest mark.

highest = 'F'

for a in range(len(sub_grade)):
	if sub_grade[a][1] < highest:
		highest = sub_grade[a][1]
	if sub_grade[a][1] == highest:
		subject = sub_grade[a][0]

print "The highest mark is in", subject



# The second algorithm outputs each subject and the grade symbol in the format 'subject: symbol', with each subject on a single line.

for a in range(len(sub_grade)):
	subject = sub_grade[a][0]
	symbol = sub_grade[a][1]
	print subject + ':' + symbol
	

# The third algorithm prints out a tab separated list of subjects on the first line, and the corresponding grades, also tab separated on the second line.

subjects = ''
symbols = ''
for a in range(len(sub_grade)):
	subject = sub_grade[a][0]
	subjects = subjects + subject + '\t' 
	symbol = sub_grade[a][1]
	symbols = symbols + symbol + '\t' 
	
print subjects
print symbols

