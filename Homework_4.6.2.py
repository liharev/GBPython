#Homework 4.6.2
from itertools import cycle
from sys import argv
script, finish = argv
ilist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
count = 0
for el in cycle(ilist):
    if count > int(finish):
        break
    else:
        print(el)
        count += 1
print("Конец программы")