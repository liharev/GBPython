#Homework 4.5
from functools import reduce
nums = [num for num in range(100,1001) if num%2 == 0]
mult = reduce(lambda x,y: x * y, nums)
print(f"Произведение четных числе от 100 до 100 = {mult}")
print("Конец программы")