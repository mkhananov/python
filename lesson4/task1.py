from sys import argv


def salary(hours, rate, bonus):
    return int(hours) * int(rate) + int(bonus)


print("Заработная плата:", salary(argv[1], argv[2], argv[3]))
