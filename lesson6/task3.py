class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return print("Сотрудник:", self.name, self.surname, "на должности:", self.position)

    def get_total_income(self):
        return print("Заработная плата:", sum(list(map(int, self._income.values()))))


my_name = input("Введите имя сотрудника: ")
my_surname = input("Введите его фамилию: ")
my_position = input("Введите его должность: ")
my_wage = input("Его оклад: ")
my_bonus = input("И премию: ")

p = Position(my_name, my_surname, my_position, my_wage, my_bonus)
p.get_full_name()
p.get_total_income()
