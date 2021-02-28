# Homework 8.2

class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

while True:
    a = input("Введите делимое, выход q: ")
    if a == "q":
        break
    b = input("Введите делитель, выход q: ")
    if b == "q":
        break
    try:
        if int(b) == 0:
            raise MyZeroDivisionError("Нельзя делить на ноль!")
        c = int(a)/int(b)
    except ValueError:
        print("Введены не числа!")
    except MyZeroDivisionError as err:
        print(err)
    else:
        print(f"Результат деления равен: {c}")


print("Конец программы")