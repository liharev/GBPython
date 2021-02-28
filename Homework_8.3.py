# Homework 8.3
mylist = []

class MyValueError(ValueError):
    def __init__(self, txt):
        print(txt)

while True:
    try:
        new_elem = input("Введите число, выход q: ")
        if new_elem == "q":
            break
        if not new_elem.isdigit():
            raise MyValueError("Введено не число!")
    except MyValueError:
        continue
    else:
        mylist.append(new_elem)

print(f"Финальный список: {mylist}")
print("Конец программы")