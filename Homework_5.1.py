# Homework 5.1
myfile = open("Homework_5.1.txt",'w')
str = input(">")
while str != (''):
    myfile.write(str+"\n")
    str = input(">")
myfile.close()
print("Конец программы!")