# Homework 7.2
class Clothes:
    material = 0

    @property
    def getmaterial(self):
        return self.material

    pass

class Coat(Clothes):

    def __init__(self,v):
        self.material = round(v/6.5+0.5,2)

class Suit(Clothes):

    def __init__(self,h):
        self.material = round(h*2+0.3,2)

c = Coat(int(input("Введите размер для пальто: ")))
print(f"Для пальто требуется материала: {c.material}")
s = Suit(int(input("Введите размер для костюма: ")))
print(f"Для костюма требуется материала: {s.material}")
print("Конец программы")