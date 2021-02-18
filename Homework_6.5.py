# Homework 6.5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Тонкая синяя линия")

class Pencil(Stationery):
    def draw(self):
        print("Тонкая серая линия")

class Handle(Stationery):
    def draw(self):
        print("Широкая красная линия")

pencil = Pencil("Pencil")
pen = Pen("Pen")
handle = Handle("Handle")

pen.draw()
pencil.draw()
handle.draw()

print("Конец программы!")