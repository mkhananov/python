print("Практическое задание 4.\nВывод максимальной цифры из числа.")
number = int(input("Введите любое целое положительное число: "))
digit = 0
while number != 0:
    if (number % 10) > digit:
        digit = number % 10
    number = number // 10
print("Максимальная цифра в этом числе", digit)