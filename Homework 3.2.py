#Homework 3.2
personaldata = {"имя":'', "фамилию":'', "год рождения":'', "город":'', "эл.почту":'', "телефон":''}
def printpersonaldata(a, b, c, d, e, f):
    print(f"Имя: {a}, Фамилия: {b}, Год рождения: {c}, Город: {d}, E-mail: {e}, Телефон: {f}")
for i in personaldata:
    personaldata[i] = input(f"Введите {i}: ")
printpersonaldata(a=personaldata.get("имя"), \
                  b=personaldata.get("фамилию"), \
                  c=personaldata.get("год рождения"), \
                  d=personaldata.get("город"), \
                  e=personaldata.get("эл.почту"), \
                  f=personaldata.get("телефон"))
print("Конец программы")