import random
import os
ship_size = 4
dimension = 10

#Setup the display board
board = []
for row in range(dimension):
	row_list=[]
	for col in range(dimension):
		row_list.append(" ")
	board.append(row_list)

#Selecting row, col, and orientation randomly
#Orientation = 0 means down
#Orientation = 1 means right
col_select = random.randint(0,9)
if col_select > 6:
	row_select = random.randint(0,6)
	orientation = 0
else:
	row_select = random.randint(0,9)
	if row_select > 6:
		orientation = 1
	else:
		orientation = random.randint(0,1)

#Create another board to store the placement of the ship.
board1 = []
for row in range(dimension):
	row_list=[]
	for col in range(dimension):
		row_list.append(" ")
	board1.append(row_list)

#Place the ship into the board
row_storage = row_select
col_storage = col_select
board1[row_select][col_select] = '*'
if orientation == 0:
	for i in range(ship_size-1):
		row_select = row_select +1
		board1[row_select][col_select] = '*'
else:
	for i in range(ship_size-1):
		col_select = col_select + 1
		board1[row_select][col_select] = '*'

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
	
#start to input player's guess
counter = 0
score = 100
while counter < 4:
	guess = list(input('Enter Coordinate to Target (e.g. A1):....'))
	guess_col = ord(guess[0])-65
	while str(guess[1]).isdigit() != True or guess_col < 0 or guess_col > 9 or len(guess) > 2 :
		guess = list(input('wrong input format\n'+'Enter Coordinate to Target (e.g. A1):....'))
		guess_col = ord(guess[0])-65	
	if board1[int(guess[1])][guess_col] == '*':
		counter = counter +1
		board[int(guess[1])][guess_col] = 'X'
		os.system("clear")#clear the screen
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
	else:
		score = score - 2
		board[int(guess[1])][guess_col] = '#'
		os.system("clear")#clear the screen
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
print('game ends! the ship is sunk and your score is:' + str(score))

















