student_grades = [['John', '9', '10', '7', '6'],['Marry', '9', '8', '8'], ['Smith', '8', '4'], ['Adam', '6', '4', '7', '5', '10']]
for i  in range(4):
	cnt = 0
	grade = 0
	for j in range(6):
		cnt = cnt + 1
		grade = grade + student_grades[i][j]
	average = grade/cnt
	print(average"\n")
