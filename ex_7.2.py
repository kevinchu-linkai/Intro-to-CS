import random
random_value = random.randint(1,6)

guess = input("guess the number of the roll") 
if int(guess) == random_value:
		print('correct')
while int(guess) != random_value:
	if guess.isdigit()!=1 or int(guess)>6 or int(guess) <1:
		print('wrong input')
	else:
		print('wrong')
	guess = input("guess the number of the roll") 

print("*---*\n"+'| '+str(random_value)+' |\n'+'*---*')