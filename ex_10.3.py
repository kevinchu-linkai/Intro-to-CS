def char_frequencies(string):
	fq = {}
	list_a = list(string)
	for i in range(len(string)):
		if list_a[i] in fq:
			fq[list_a[i]] =  fq[list_a[i]] + 1
		else:
			fq[list_a[i]] =  1
	return fq 

my_string = 'Hello World'
print(char_frequencies(my_string))



'''
professor's way

my_dict = {}
for char in string:
	my_dict[char] = my_dict.get(char,0) + 1
return my_dict
'''