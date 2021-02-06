# Homework 1.5
profit = int (input("Введите значение выручки: "))
expenses = int (input("Введите значения издержек: "))
if profit > expenses:
    print(f"Компания работает с рентабельностью: {(100*(profit-expenses)/profit):.2f}%")
    employees = int(input("Сколько сотрудников в компании: "))
    print(f"Прибыль в расчете на сотрудника составляет: {((profit-expenses)/employees):.2f}")
else:
    print(f"Компания убыточна")
print("Конец программы")