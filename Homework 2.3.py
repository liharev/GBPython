#Homework 2.3
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
season = "Осень"
month = 0
seasons = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",\
           7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
while not (month in range(1,13)):
    month = int(input("Введите номер месяца (1-12): "))
if month in winter:
    season = "Зима"
elif month in spring:
    season = "Весна"
elif month in summer:
    season = "Лето"
print("Решение через списки. Месяц номер ", month," это - ", season)
print("Решение через словарь круче. Результат - ", seasons.get(month))
print("Конец программы!")