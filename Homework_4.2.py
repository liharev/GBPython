# Homework 4.2
ilist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
rlist = [num for num in ilist[1::] if ilist[ilist.index(num)-1] < num]
print(rlist)
print("Конец программы")