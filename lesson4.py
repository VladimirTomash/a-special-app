number = int(input('Enter a number: '))
summa = 0
while number != 0:
    last_num = number % 10
    summa += last_num
    print(number)
    if last_num == 5:
        print('gap detected')
        break
    number //= 10
    print('current sum of numbers ', summa)
print('\nGrand total of numbers: ', summa)
# print('hh')