input_file = open('red.txt', 'r')
red = 0
blue = 0
for line in input_file:

	if 'red' in line:
		red = red +1

	if 'blue' == line:
		blue = blue +1

input_file.close()
print(red)
print(blue)