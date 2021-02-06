# Homework 1.4
number = int (input("Введите введите целое положительное число: "))
maximum = 0
while number > 0:
    if number%10 > maximum:
        maximum = number%10
    number = number//10
print(f"Максимальная цифра в введенном числе: {maximum}")
print("Конец программы")