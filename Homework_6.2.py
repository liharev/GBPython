# Homework 6.2
class Road():
    def __init__(self, length, width):
        self.__lenght = int(length)
        self.__width = int(width)

    def weight(self, mass, depth):
        return self.__lenght*self.__width*int(mass)*int(depth)/100

length, width = input("Введите через пробел длину и ширину дорожного покрытия в метрах: ").split()
r = Road(length, width)
mass, depth = input("Введите через пробел массу кг. одного кв.м. покрытия тощиной 1 см и толщину покрытия в см.: ").split()
print(f"Масса дорожного покрытия = {r.weight(mass,depth)/1000} тонн")
print("Конец программы!")