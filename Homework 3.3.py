#Homework 3.3
my_func = lambda a, b, c: max(a+b, b+c, a+c)
a, b, c = (float(i) for i in input("Введите три числа через пробел: ").split())
print(my_func(a,b,c))
print("Конец программы")