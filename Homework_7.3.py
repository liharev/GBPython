# Homework 7.3
class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return self.nucleus + other.nucleus

    def __sub__(self, other):
        dif = self.nucleus - other.nucleus
        if dif >= 0:
            return dif
        else:
            raise RuntimeError("Ошибка! Разность клеток меньше нуля")

    def __mul__(self, other):
        return self.nucleus * other.nucleus

    def __truediv__(self, other):
        return round(self.nucleus/other.nucleus)


a = Cell(int(input("Введите число ядер первой клетки: ")))
b = Cell(int(input("Введите число ядер второй клетки: ")))
c = Cell(0)
while True:
    choice = input("1: Сложить клетки, 2: Вычесть, 3: умножить, 4: разделить, иное - выход: ")
    if 0 < int(choice) < 5:
        print("Ok")
        if int(choice) == 1:
            c.nucleus = a + b
        elif int(choice) == 2:
            c.nucleus = a - b
        elif int(choice) == 3:
            c.nucleus = a * b
        else:
            c.nucleus = a / b
        print(c.nucleus)
    else:
        break

print("Конец программы")