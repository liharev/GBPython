#Homework 3.1
def division(a, b):
    if b !=0:
        return a/b
    else:
        return "Exception"
a, b = (int(i) for i in input("Введите два числа через пробел: ").split())
res = division(a,b)
if  res == "Exception":
    print("Ошибка! Деление на 0")
else:
    print(res)
print("Конец программы")
