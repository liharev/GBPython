# Homework 1.6
a = float (input("Введите начальное значение (км): "))
b = float (input("Введите целевое значение (км): "))
n = 1
while a<b:
    a = a*1.1
    n = n+1
print(f"Спортсмен пробежит {b} км. на {n} день")
print("Конец программы")


