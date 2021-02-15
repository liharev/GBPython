# Homework 5.4
from num2words import num2words
source = open("Homework_5.4.1.txt",'r')
result = open("Homework_5.4.2.txt",'w')
for str in source:
    elements = str.split()
    num = int(elements[2])
    record = num2words(num, lang='ru') + " — " + elements[2]+"\n"
    result.write(record)
source.close()
result.close()
print("Конец программы!")