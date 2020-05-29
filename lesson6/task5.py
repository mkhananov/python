class Stationery:
    title = "Запуск отрисовки"

    def draw(self):
        print(self.title, "чем придется")


class Pen(Stationery):
    def draw(self):
        print(self.title, "ручкой")


class Pencil(Stationery):
    def draw(self):
        print(self.title, "карандашом")


class Handle(Stationery):
    def draw(self):
        print(self.title, "маркером")


Pen().draw()
Pencil().draw()
Handle().draw()


