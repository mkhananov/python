print("Практическое задание 3."
      "\nСезон по номеру месяца.")

user_month = int(input("Введите номер месяца: "))
while user_month not in range(1, 13):
    user_month = int(input("Должо быть целое число от 1 до 12. Введите номер месяца: "))

seasons = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

for season, months_in_the_season in seasons.items():
    for one_of_the_months in months_in_the_season:
        if one_of_the_months == user_month:
            print("Сезон:", season)
