# Homework 5.5
from random import randint
def sumlist(numList):
    summa = 0
    for i in numList:
        summa = summa + int(i)
    return summa
myfile = open("Homework_5.5.txt",'w')
for _ in range(1,100):
    myfile.write((str(randint(-100,100))+" "))
myfile.close()
myfile = open("Homework_5.5.txt",'r')
print(f"Сумма всех чисел в файле = {sumlist(myfile.read().split())}")
myfile.close()
print("Конец программы!")