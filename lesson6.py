def sum_factorials(num):
    part_factorial = 1
    summa = 0

    for i in range(1, num + 1):
        part_factorial *= i  # multiplies every term of the sequence on last term
        summa += part_factorial
    return summa


n = int(input('enter a number: '))
print(sum_factorials(n))
