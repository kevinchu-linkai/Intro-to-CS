import random
import os
import time
dimension = 10

board = []
for row in range(dimension):
	row_list=[]
	for col in range(dimension):
		row_list.append(" ")
	board.append(row_list)


counter = 0
while counter < 5:
	x = random.randint(0,9)
	y = random.randint(0,9)
	if board[x][y] == 'X':
		x = random.randint(0,9)
		y = random.randint(0,9)
	else:
		board[x][y] = 'X'
		counter = counter + 1

os.system('clear')

#To print the board for user to see
for col in range(dimension):
	col_into_alpha = chr(col+65)
	print('   ' + col_into_alpha, end= ' ' )
print("\n +" + "----+" * dimension)
for row in range(dimension):
	print(str(row) + '|', end=' ')
	for col in range(dimension):
		print(' '+board[row][col] + ' |', end=' ')
	print("\n +"+"----+"*dimension)

for i in range(10):
	for r in range(dimension-2, -1, -1):
		for c in range(dimension):
			if board[r][c] == 'X' and board[r+1][c] != 'X':
				board[r+1][c] = board[r][c]
				board[r][c] = ' '
	time.sleep(1)

	os.system('clear')

	#To print the board for user to see
	for col in range(dimension):
		col_into_alpha = chr(col+65)
		print('   ' + col_into_alpha, end= ' ' )
	print("\n +" + "----+" * dimension)
	for row in range(dimension):
		print(str(row) + '|', end=' ')
		for col in range(dimension):
			print(' '+board[row][col] + ' |', end=' ')
		print("\n +"+"----+"*dimension)





