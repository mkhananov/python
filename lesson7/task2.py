from abc import abstractmethod


class Clothes:
    def __init__(self, var, count):
        self.var = float(var)
        self.count = int(count)

    @abstractmethod
    def outlay(self):
        pass


class Coat(Clothes):
    @property
    def outlay(self):
        return round((self.var / 6.5 + .5) * self.count, 2)


class Suite(Clothes):
    @property
    def outlay(self):
        return (self.var * 2 + .3) * self.count


coat_size = input("Введите размер пальто: ")
coats_count = input("Введите количество пальто, которые необходимо пошить: ")

suit_size = input("Введите размер комстюма: ")
suits_count = input("Введите количество комстюмов, которые необходимо пошить: ")

coats_outlay = Coat(coat_size, coats_count).outlay
suites_outlay = Suite(suit_size, suits_count).outlay

print("Расход ткани на пошив пальто: ", coats_outlay)
print("Расход ткани на пошив костюмов: ", suites_outlay)
print("Общий расход ткани: ", coats_outlay + suites_outlay)
