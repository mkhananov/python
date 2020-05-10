print("Практическое задание 5.\nОпределение финансового результата работы фирмы.")
takings = int(input("Введите выручку фирмы за период: "))
costs = int(input("Введите издержки фирмы за период: "))
if takings < costs:
    print("Фирма потерпела убытки в размере", costs - takings)
elif takings > costs:
    profit = takings - costs
    employees = int(input("Введите количество сотрудников: "))
    print("Прибыль фирмы", profit)
    print("Рентабельность выручки", profit / takings)
    print("Прибыль фирмы в расчете на одного сотрудника", profit / employees)
else:
    print("Фирма сработала в ноль")


