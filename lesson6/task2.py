class Road:
    _weight = 25
    _depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road(self):
        return int(self._length) * int(self._width) * self._depth * self._weight / 1000


my_length = input("Введите длину дорожного полотна в м: ")
my_width = input("Введите ширину дорожного полотна в м: ")
w = Road(my_length, my_width)
print("Масса дорожного полотна на тощину 5 см =", w.weight_road(), "т")
