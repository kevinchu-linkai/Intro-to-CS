def unique_list(list_input):
	output = []
	for x in list_input:
		if x not in output:
			output.append(x)

	return output

list_a = [1,2,3,3,3,4,4,4,4,9,8,8,9,3,4,5,2,5,1]
list_b = unique_list(list_a)
print(list_b)