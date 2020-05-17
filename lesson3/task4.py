print("Практическое задание 4")
var_1 = 20
var_2 = -2


def method_1(x, y):
    return x ** y


def method_2(x, y):
    result = x
    for _ in range(1, abs(y)):
        result *= x
    return 1 / result


print(f"Возведение числа {var_1} в степень {var_2} через '**', результат:", method_1(var_1, var_2))
print(f"Возведение числа {var_1} в степень {var_2} через 'for in', результат:", method_2(var_1, var_2))
