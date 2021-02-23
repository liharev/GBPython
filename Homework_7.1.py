# Homework 7.1
class Matrix:
    elements = []

    def __init__(self, data):
        self.elements = data

    def __str__(self):
        newstr = ""
        for el in self.elements:
            newstr += "\n"+str(el)
        return newstr

    def __add__(self, other):
        res = []
        for r in self.elements:
            res.append([])
            for el in r:
                res[self.elements.index(r)].append(el + other.elements[self.elements.index(r)][r.index(el)])
        return res



am = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
bm = Matrix([[4, 4, 4], [5, 5, 5], [6, 6, 6]])
print(f"Первая матрица {am}")
print(f"Вторая матрица {bm}")
cm = Matrix(am+bm)
print(f"Результат сложения матриц {cm}")
print("Конец программы")
