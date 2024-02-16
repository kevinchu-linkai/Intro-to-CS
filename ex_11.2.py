cnt = 0
add = 0
try:
	input_file = open("ex_11.2_intnumbers.txt", 'r')
	for line in input_file:
		try:
			add = add + int(line.strip())
			cnt = cnt + 1
		except ValueError:
			print('non-numeric data found:'+line.strip())
	avg = add / cnt
	print(avg)
	input_file.close()

except FileNotFoundError:
	print('file not found')

except ZeroDivisionError:
	print('no numeric data')
	input_file.close()

except:
	print('error')

print('bye')
