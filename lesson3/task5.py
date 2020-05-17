print("Практическое задание 5")
result, repeat = 0, 1

while repeat == 1:
    arr = input("Введите строку чисел разделенных пробелом: ").split(" ")
    for el in arr:
        try:
            result += int(el)
        except ValueError:
            repeat = 0
            break
    print("Итоговая сумма", result)
