file_name = '3AYU.pdb'
test = open('test.pdb', 'r')
option = 'H'
aaA = ''
aaB = ''
for line in test:
	if option == 'H':
		if 'SEQRES' in line:
			chain = line[11]
			if chain == 'A':
				aaA = aaA + line[19:].rstrip() + ' '
			else:
				aaB = aaB + line[19:].rstrip() + ' '	



aa = aaA + aaB

aa = aa.split(' ')
aa = aa[0:-1]


def histogram(his):
    store_aa = {}
    for x in his:
        if x in store_aa:
            store_aa[x] += 1
        else:
            store_aa[x] = 1
    return store_aa

his_aa = histogram(aa)
his_aa = his_aa.items()
print his_aa
print 'Choose an option to order by: ', '\b\n', '   number of amino acids - ascending (an)', '\b\n', '   number of amino acids - ascending (an)', '\b\n', '   alphabetically - ascending        (aa)', '\b\n', '   alphabetically - descending       (da)', '\b\n',

order = raw_input('order by: ')

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
		

