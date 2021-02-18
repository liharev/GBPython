# Homework 6.1
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = "красный"
        self.colors = {7: "красный", 2: "желтый", 3: "зеленый"}

    def running(self):
        for item in self.colors:
            self.__color = self.colors[item]
            print(f"Цвет светофора: {self.__color} {item} секунд")
            sleep(int(item))
        self.__color = "красный"
        print(f"Цвет светофора: {self.__color}")


tl = TrafficLight()

while input("Нажмите любую клавишу, q - выход: ") != "q":
    tl.running()

print("Конец программы!")
