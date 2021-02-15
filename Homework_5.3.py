# Homework 5.3
myfile = open("Homework_5.3.txt",'r')
FOT = 0
employees = 0
for str in myfile:
    name, salary = str.split()
    salary = int(salary)
    FOT = FOT+salary
    employees += 1
    if salary < 20000:
        print(f"{name} имеет ЗП менее 20000")
print(f"Средняя ЗП по компании: {FOT/employees}")
myfile.close()
print("Конец программы!")