action = input('enter the action: ')
first_number = int(input('enter the first number: '))
second_number = int(input('enter the second number: '))
if action == "+":
	expression = str(first_number) + ' + ' + str(second_number) + ' = '
	equation = first_number + second_number
elif action == '-':
	expression = str(first_number) + ' - ' + str(second_number) + ' = '
	equation = first_number - second_number
else:
	print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
	exit()
print(expression, equation)