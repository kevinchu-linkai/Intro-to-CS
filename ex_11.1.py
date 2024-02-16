birthday = {}
name = 'null'
def instruction():
	command = int(input(
'1. look up a birthday\n'+ 
'2. add a new birthday\n'+ 
'3. change a birthday\n'+
'4. delete a birthday\n'+ 
'5. quit the program\n'))
	return command

#def lookup():
input_file = open('birthday.csv','a')
input_file.close()
input_file = open('birthday.csv','r')
for line in input_file:
	name , day = line.strip().split(',')
	birthday[name] = day
input_file.close()

output_file = open('birthday.csv','w')
i = 0
while i != 1:
	x = instruction()
	if x == 1:
		name = input('put in the name of the person:')
		print(birthday.get(name,'not found'))
		print(birthday)
	elif x == 2:
		name = input('put in the name of the person:')
		birthday[name] = input('put in the birthdy of the person:')
		print(birthday)
	elif x == 3:
		name = input('put in the name of the person:')
		birthday[name] = input('put in the birthdy of the person:')
		print(birthday)
	elif x == 4:
		name = input('put in the name of the person:')
		birthday.pop(name)
		print(birthday)
	elif x == 5:
		for name in birthday:
			output_file.write(name+','+birthday[name]+ '\n')
		output_file.close()
		exit()
	else:
		print('wrong input')