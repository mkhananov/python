print("Практическое задание 3.\nВведеное Вами число вычислится по формуле n + nn + nnn.")
number = input("Введите число: ")
print("Результат выражения n + nn + nnn:", int(number) + int(number + number) + int(number + number + number))