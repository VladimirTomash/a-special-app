def sum_factorials(num):
    part_factorial = 1
    summa = 0
    print(summa)
    for i in range(1, num + 1):
        part_factorial *= i  # multiplies every term of the sequence on last term
        summa += part_factorial  # added previous term to total sum
    return summa


n = int(input('enter a number: '))
print(sum_factorials(n))
