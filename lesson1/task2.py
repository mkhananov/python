print("Практическое задание 2")
time = int(input("Введите количество секунд: "))
seconds = time % 60
minutes = (time // 60) % 60
hours = (time // 3600) % 24
days = time // (3600 * 24)
if days == 0:
    print(f"Переведено в формат чч:мм:сс - {hours:02}:{minutes:02}:{seconds:02}")
else:
    print(f"Переведено в формат дней и чч:мм:сс - {days} д. {hours:02}:{minutes:02}:{seconds:02}")


