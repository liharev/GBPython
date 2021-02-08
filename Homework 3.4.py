#Homework 3.4
number = 0
power = 0
my_func1 = lambda x, y: 1/x**(-y)
def my_func2(x, y):
    z = 1
    for i in range(-y):
        z = z*x
    return 1/z
while not (number > 0 and power < 0):
    number, power = (int(i) for i in input("Введите два число (>0) и степень (<0) через пробел: ").split())
print(f"Решение через lambda функцию и оператор возведения в степень: {my_func1(number, power)}")
print(f"Решение через функцию и цикл: {my_func2(number, power)}")
print("Конец программы")