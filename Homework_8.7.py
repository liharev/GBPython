# Homework 8.7

def form_complex(a, b):
    if b > 0:
        c = str(round(a, 1)) + "+" + str(round(b, 1)) + "*j"
    elif b < 0:
        c = str(round(a, 1)) + str(round(b, 1)) + "*j"
    else:
        c = str(a)
    return c

class complex_number():
    def __init__(self, a):
            a = complex (a)
            self.real = a.real
            self.imag = a.imag
            self.complex = form_complex(self.real, self.imag)

    def __add__(self, other):
        a = self.real + other.real
        b = self.imag + other.imag
        return form_complex(a, b)

    def __mul__(self, other):
        a = self.real*other.real - self.imag*other.imag
        b = self.imag*other.real + self.real*other.imag
        return form_complex(a, b)

while True:
    try:
        x = complex_number(input("Введите первое комплексное число в виде a+b*j, где a и b - числа: "))
        y = complex_number(input("Введите второе комплексное число в виде a+b*j, где a и b - числа: "))
    except ValueError:
        print("\033[91m {}\033[00m".format("Ошибка ввода!"))
        continue
    print(f"Результат сложения: ({x.complex})+({y.complex}) = {x+y}")
    print(f"Результат умножения: ({x.complex})*({y.complex}) = {x*y}")
    if input("Продолжить - Y, иначе - выход: ") != "Y":
        break

print("Конец программы")