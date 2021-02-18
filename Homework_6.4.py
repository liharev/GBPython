# Homework 6.4
from random import randint
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")

    def go(self, speed):
        self.speed = speed
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f"{self.name} не движется")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")
        if self.speed > 60:
            print("Превышение!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")
        if self.speed > 40:
            print("Превышение!")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

tc = TownCar(0, "White", "Honda", False)
wc = WorkCar(0, "Yellow", "Renault", False)
sc = SportCar(0, "Red", "Lamborghini", False)
pc = PoliceCar(0, "Black", "Ford", True)
cars = [tc, wc, sc, pc]

while input("Нажмите любую клавишу, q - выход: ") != "q":
    for car in cars:
        print(f"{car.name}, цвет {car.color}:")
        car.go(randint(0,150))
for car in cars:
    car.stop()

print("Конец программы!")
