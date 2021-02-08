#Homework 3.6
int_func = lambda a: a.capitalize()
def int_func1(a):
    alist = a.split()
    for i in alist:
        alist[alist.index(i)] = int_func(i)
    return ' '.join(alist)
word = int_func(input("Введите слово: "))
print(word)
sentence = int_func1(input("Введите предложение: "))
print(sentence)
print("Конец программы")