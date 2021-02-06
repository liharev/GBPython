#Homework 2.6
specification = ["Название: ", "Цена: ", "Количество: ", "Ед: "]
position = {}
goods = []
analytics = {}
astr = []
count = 0
a = "Y"
while a == "Y":
    for i in specification:
        position.setdefault(i, input(i))
    count += 1
    goods.append(((count,) + (dict(position),)))
    position.clear()
    a = input("Продолжить? (Y/n): ")
for i in specification:
    for k in goods:
        if k[1].get(i) in astr:
            continue
        else:
            astr.append(k[1].get(i))
    analytics[i] = list(astr)
    astr.clear()
print(analytics)
print("Конец программы!")


