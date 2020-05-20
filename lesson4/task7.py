def fact(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
        yield factorial


n = int(input("Введите число для которого будет рассчитан факториал: "))
for el in fact(n):
    print(el)
