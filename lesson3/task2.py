print("Практическое задание 2")
user_name = "Михаил"
user_surname = "Хананов"
user_yob = 1984
user_city = "Сочи"
user_email = "mkhananov@gmail.com"
user_phone = 79628810084


def my_func(name, surname, yob, city, email, phone):
    return print(f"{name} {surname}, {yob} года рождения, проживающий в г. {city}, e-mail: {email}, тел.: {phone}")


my_func(name=user_name, surname=user_surname, yob=user_yob, city=user_city, email=user_email, phone=user_phone)
