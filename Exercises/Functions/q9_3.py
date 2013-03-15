# The program asks the user for a space separated list of data points (i.e. floating point numbers), then uses appropriate functions from previous questions to calculate and output the standard deviation of those numbers. 

flt = raw_input('Enter a list of space separated float point numbers: ')

def mean():
	list1 = flt.split(' ')
	total = 0
	for a in list1:
		total = total + float(a)
	return total/(len(list1))

summation = 0
list2 = flt.split(' ')
for a in list2:
	summation = summation + ((float(a) - mean())**2)

from math import sqrt
st_dev = sqrt(summation/len(list2))
print st_dev



