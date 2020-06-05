import random
import re


class LotoCard:
    def __init__(self, player):
        self.player, self.ticket, self.numbers, self.len_row, numbers_per_row, count_row = player, [], 90, 9, 5, 3
        self.my_list = list(range(1, self.numbers + 1))
        for n in range(count_row):
            row = []
            for el in range(numbers_per_row):
                del_el = self.my_list[random.randrange(len(self.my_list))]
                self.my_list.remove(del_el)
                row.append(del_el)
            row = sorted(row)
            for el in range(self.len_row - numbers_per_row):
                row.insert(random.randrange(len(row)), "")
            self.ticket += row

    def __str__(self):
        my_str = ""
        if self.player == "Компьютер":
            my_str = "\n------ Карточка компьютера -------\n"
        if self.player == "Игрок":
            my_str = "\n--------- Ваша карточка ----------\n"
        n = 1
        for m in self.ticket:
            digits = str(m)
            if len(digits) == 1:
                digits = " " + digits
            my_str += digits
            if n % self.len_row == 0:
                my_str += "\n"
            else:
                my_str += "\t"
            n += 1
        my_str += "-" * 34
        return my_str


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.numbers = 90

    def start(self):

        p1 = str(self.player1)
        p2 = str(self.player2)
        end_game = 0
        bag_barrels = list(range(1, self.numbers + 1))
        left_barrels = len(bag_barrels)
        while left_barrels != 0 or end_game == 0:
            take_barrel = bag_barrels[random.randrange(left_barrels)]
            bag_barrels.remove(take_barrel)
            take_barrel = str(take_barrel).rjust(2, " ")
            left_barrels = len(bag_barrels)
            print(p1, p2, f"\nНовый бочонок: {take_barrel} (осталось {left_barrels})")
            answer = input("Зачеркнуть цифру? (y/n): ")
            if not re.findall(take_barrel, p1):
                if answer == "y":
                    print("Этого числа не было, Вы проиграли!")
                    end_game = 1
            else:
                if answer == "n":
                    print("Вы не заметили число, уже не выйграите!")
                    end_game = 1
            p1 = re.sub(take_barrel, "--", p1)
            p2 = re.sub(take_barrel, "--", p2)

            if not re.findall("\d", p1) and not re.findall("\d", p2):
                print("Ничья...?")
                end_game = 1
                continue

            if not re.findall("\d", p2):
                print("Вы програли!")
                end_game = 1

            if not re.findall("\d", p1):
                print("Вы выйграли!")
                end_game = 1

            if not re.findall("\d", p2):
                print("Вы програли!")
                end_game = 1


human_player = LotoCard("Игрок")
computer_player = LotoCard("Компьютер")
game = Game(human_player, computer_player)
game.start()
