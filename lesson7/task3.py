class Cell:
    def __init__(self, cells):
        self.cells = cells

    def make_order(self, count):
        my_str = ""
        for el in range(self.cells):
            if el % count == 0:
                my_str += "\n"
            my_str += "*"
        return my_str

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __str__(self):
        return str(self.cells)


a = Cell(int(input("Количество ячеек первой клетки: ")))
b = Cell(int(input("Количество ячеек второй клетки: ")))
n = int(input("Количество ячеек в ряду: "))
print("\nРезультат сложения клеток:", a + b, (a + b).make_order(n))
print("\nРезультат вычитания клеток:", a - b, (a - b).make_order(n))
print("\nРезультат умножения клеток:", a * b, (a * b).make_order(n))
print("\nРезультат деления клеток:", a / b, (a / b).make_order(n))
