#Homework 2.5
mylist = [7, 5, 3, 3, 2]
newrating = 0
while newrating != "quit":
    newrating = input("Введите новое значение рейтинга, выход - quit: ")
    if newrating.isdigit():
        mylist.append(int(newrating))
    elif newrating != "quit":
        print("Ошибка: Значение должно быть целым положительным числом!")
    mylist = sorted(mylist, reverse = True)
    print(mylist)
print("Конец программы!")