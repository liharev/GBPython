#Homework 3.5
arg_elements = []
current_sum = 0
stop = False
def summator(summa, arg_str):
    sum_stop = False
    arg_elements = arg_str.split()
    for a in arg_elements:
        if a.isdigit():
            summa = summa + float(a)
        else:
            sum_stop = True
            break
    return summa, sum_stop
while stop == False:
    a = input("Введите числа для суммирования через пробел: ")
    current_sum, stop = summator(current_sum, a)
    print(f"Сумма = {current_sum}")
print(f"Результат = {current_sum}")
print("Конец программы")
