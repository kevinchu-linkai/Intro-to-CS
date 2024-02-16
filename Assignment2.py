import os
import random

#create a function to print the board
def print_board(list):
	for col in range(dimension2):
		col_into_alpha = chr(col+65)
		print('   ' + col_into_alpha, end= ' ' )
	print("\n +" + "----+" * dimension2)
	for row in range(dimension1):
		print(' |', end=' ')
		for col in range(dimension2):
			print(' '+board[row][col] + ' |', end=' ')
		print("\n +"+"----+"*dimension2)

#create a function to check the horizontal line of 4 checkers
def right(a_list):
	for row in range(len(a_list)):
		for col in range(len(a_list[0])-4):
			if a_list[row][col] != ' ':
				cnt = 1
				while a_list[row][col+cnt] == a_list[row][col]:
					cnt += 1
					if cnt == 4:
						return 1
				cnt = 1
	return 0

#create a function to check vertical line of 4 checkers
def down(a_list):
	for row in range(len(a_list)-3):
		for col in range(len(a_list[0])):
			if a_list[row][col] != ' ':
				cnt = 1
				while a_list[row+cnt][col] == a_list[row][col]:
					cnt += 1
					if cnt == 4:
						return 1
				cnt = 1
	return 0

#create a function to check left_downward line of 4 checkers
def leftdown(a_list):
	for row in range(len(a_list)-3):
		for col in range(3,len(a_list[0])):
			if a_list[row][col] != ' ':
				cnt = 1
				while a_list[row+cnt][col-cnt] == a_list[row][col]:
					cnt += 1
					if cnt == 4:
						return 1
				cnt = 1
	return 0

#create a function to check right_downward line of 4 checkers
def rightdown(a_list):
	for row in range(len(a_list)-3):
		for col in range(len(a_list[0])-4):
			if a_list[row][col] != ' ':
				cnt = 1
				while a_list[row+cnt][col+cnt] == a_list[row][col]:
					cnt += 1
					if cnt == 4:
						return 1
				cnt = 1
	return 0

#create a function to check draw
def draw(a_list):
	cnt = 1
	for row in range(len(a_list)):
		for col in range(len(a_list[0])):
			if a_list[row][col] != ' ':
				cnt += 1
			if cnt == dimension2*dimension1:
				return 1
	return 0

'''create a function to assign different checkers for players to place 
and print the board after every placement'''
def player_check(num):
	if num == 1:
		check = 'X'
	elif num == 2:
		check = 'O'
	elif num == 3:
		check = 'V'
	elif num == 4:
		check = 'H'
	elif num == 5:
		check = 'M'
	for i in range(dimension1):
		if board[0][place] != ' ':	
			os.system('clear')
			print_board(board)
			print('the col is full and you lose your chance\n')
			return
		if board[dimension1 -1][place] == " ":
			board[dimension1 -1][place] = check
			break
		elif board[dimension1 - i-1][place] == " " and board[dimension1 - i][place] != " ":
			board[dimension1 - i-1][place] = check
			break
	os.system('clear')
	print_board(board)

os.system('clear')
#setup of the game eith inpu info
#at the same time recognize false input
dimension1 = input('enter the rows(in single number equal or bigger than 6 eg. 6):\n')
while not dimension1.isdigit():
	dimension1 = input('enter a row number equal or bigger than 6:\n')
if dimension1.isdigit():
	dimension1 = int(dimension1)
while dimension1 < 6 :
	dimension1 = int(input('enter a row number equal or bigger than 6:\n'))

dimension2 = input('enter the cols(in single number equal or bigger than 7 eg. 7):\n')
while not dimension2.isdigit():
	dimension2 = input('enter a col number equal or bigger than 7:\n')
if dimension2.isdigit():
	dimension2 = int(dimension2)
while dimension2 < 7 :
	dimension2 = int(input('enter a col number equal or bigger than 7:\n'))

players = input('the number of players(in single number between 2 and 5 eg. 2):\n')
while not players.isdigit():
	players = input('enter a row number between 2 and 5:\n')
if players.isdigit():
	players = int(players)
while players < 2 or players > 5:
	players = int(input('enter the number of players between 2 and 5:\n'))

#Setup the display board
board = []
for row in range(dimension1):
	row_list=[]
	for col in range(dimension2):
		row_list.append(" ")
	board.append(row_list)

print_board(board)

#start to place checkers by calling function
round_counter = 0
result = 0
if players == 2:
	round_counter = random.randint(1,2)
	while result == 0:
		place = input('Enter the column you want to place your checker (e.g. A):....')
		while len(place) > 1 or ord(place) < 65 or ord(place) > (dimension2+65):
			place = input('Please only enter a single capital letter in the range:')
		place = ord(place) - 65
		if round_counter % 2 != 0:
			player_check(1)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player X wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		else:
			player_check(2)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player O wins the game!')
			if dw == 1:
				result = 1
				print('draw!')

elif players == 3:
	round_counter = random.randint(1,3)
	while result == 0:
		place = input('Enter the column you want to place your checker (e.g. A):....')
		while len(place) > 1 or ord(place) < 65 or ord(place) > (dimension2+65):
			place = input('Please only enter a single capital letter in the range:')
		place = ord(place) - 65
		if round_counter % 3 == 0:
			player_check(3)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player V wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 3 == 1:
			player_check(1)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player X wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		else:
			player_check(2)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player O wins the game!')
			if dw == 1:
				result = 1
				print('draw!')

elif players == 4:
	round_counter = random.randint(1,4)
	while result == 0:
		place = input('Enter the column you want to place your checker (e.g. A):....')
		while len(place) > 1 or ord(place) < 65 or ord(place) > (dimension2+65):
			place = input('Please only enter a single capital letter in the range:')
		place = ord(place) - 65
		if round_counter % 4 == 0:
			player_check(4)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player H wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 4 == 1:
			player_check(1)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player X wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 4 == 2:
			player_check(2)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player O wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		else:
			player_check(3)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player V wins the game!')
			if dw == 1:
				result = 1
				print('draw!')

elif players == 5:
	round_counter = random.randint(1,5)
	while result == 0:
		place = input('Enter the column you want to place your checker (e.g. A):....')
		while len(place) > 1 or ord(place) < 65 or ord(place) > (dimension2+65):
			place = input('Please only enter a single capital letter in the range:')
		place = ord(place) - 65
		if round_counter % 5 == 0:
			player_check(5)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player M wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 5 == 1:
			player_check(1)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player X wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 5 == 2:
			player_check(2)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player O wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		elif round_counter % 5 == 3:
			player_check(3)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player V wins the game!')
			if dw == 1:
				result = 1
				print('draw!')
		else:
			player_check(4)
			round_counter = round_counter +1
			r = right(board)
			d = down(board)
			rd = rightdown(board)
			ld = leftdown(board)
			dw = draw(board)
			if r == 1 or d == 1 or rd == 1 or ld == 1:
				result = 1
				print('player H wins the game!')
			if dw == 1:
				result = 1
				print('draw!')



















