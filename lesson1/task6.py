print("Практическое задание 6.\nКоличество дней для достижения цели спортсменом, при увеличении длины пробежек на 10%.")
distance = float(input("Введите результат своего первого забега в км: "))
goal = float(input("Введите цель в км: "))
day = 1
increase = 1.1
while distance < goal * increase:
    print(f"{day}-й день: {distance:.2f} км")
    distance *= increase
    day += 1
print(f"На {day - 1}-й день спортсмен достигнет результата не менее {goal} км.")

