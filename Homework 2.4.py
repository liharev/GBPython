#Homework 2.4
mystr = input("Введите любую строку из нескольких слов: ")
mylist = list(mystr.split())
for i in mylist:
    print(mylist.index(i)+1,": ", i[:10])
print("Конец программы!")