def convert_temp(value,unit = "C"):

	if unit =='F':
		C = (value-32)*5/9
		print(str(C)+'C')
	elif unit == 'C':
		F = (value*9/5)+32
		print(str(F)+'F')

convert_temp(60.4,"F")