#Homework 2.2
mylist = []
mylist.append(input("Введите первый элемент списка: "))
while mylist[len(mylist)-1] != "quit":
    mylist.append(input("Введите новый элемент списка, quit - выход: "))
mylist.pop()
for i in range(0, 2*len(mylist)//2-1, 2):
    mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
print(mylist)
print("Конец программы!")
