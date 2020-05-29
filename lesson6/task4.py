class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.model = f"Автомобиль {color} {name}"
        self.is_police = is_police

    def go(self):
        print(self.model, "поехал")

    def stop(self):
        print(self.model, "остановился")

    def turn(self, direction):
        print(self.model, "повернул", direction)

    def show_speed(self):
        print("Текущая скорость", self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Текущая скорость", self.speed)
            print("Скорость превышена")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Текущая скорость", self.speed)
            print("Скорость превышена")


class PoliceCar(Car):
    pass


w_car = WorkCar(50, "Белый", "Lexus", False)
w_car.go()
w_car.turn("направо")
w_car.show_speed()
w_car.stop()
print(w_car.is_police)

p_car = PoliceCar(110, "Белый", "BMW", True)
p_car.go()
p_car.turn("налево")
p_car.show_speed()
p_car.stop()
print(p_car.is_police)

s_car = SportCar(180, "Черный", "Audi", False)
s_car.go()
s_car.turn("налево")
s_car.show_speed()
s_car.stop()
print(s_car.is_police)

w_car = TownCar(90, "Красный", "Porsche", False)

w_car.go()
w_car.turn("направо")
w_car.show_speed()
w_car.stop()
print(w_car.is_police)
