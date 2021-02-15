# Homework 5.6
def sumlist(numList):
    summa = 0
    for i in numList:
        summa = summa + int(i)
    return summa
def searchnums(str):
    l = len(str)
    nums = []
    i = 0
    while i < l:
        num = ''
        symbol = str[i]
        while '0' <= symbol <= '9':
            num += symbol
            i += 1
            if i < l:
                symbol = str[i]
            else:
                break
        i += 1
        if num != '':
            nums.append(int(num))
    return nums

myfile = open("Homework_5.6.txt",'r')
subjects = {}
for str in myfile:
    subjects[str.split(':')[0]]=sumlist(searchnums(str))
print(subjects)
myfile.close()
print("Конец программы!")