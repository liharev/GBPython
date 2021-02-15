# Homework 5.2
myfile = open("Homework_5.2.txt",'r')
for str in myfile:
    print(f"Строка: \n{str} состоит из {len(str.split())} слов")
myfile.seek(0)
print(f"Количество строк в файле: {len(myfile.readlines())}")
myfile.close()
print("Конец программы!")