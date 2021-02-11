#Homework 4.7
def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
        yield factorial
n = int(input("Введите целое положительное число: "))
for el in fact(n):
    print(el)
print("Конец программы")