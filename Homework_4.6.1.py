#Homework 4.6.1
from itertools import count
from sys import argv
script, start, finish = argv
for el in count(int(start)):
    if el > int(finish):
        break
    else:
        print(el)
print("Конец программы")