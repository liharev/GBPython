# Homework 8.1
dates = {0: 0, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_parcer(cls, date):
        cls.date = date
        day, month, year = cls.date_convertor(cls.date.split('-'))
        if day * month * year == 0:
            return "Ошибка формата даты DD-MM-YYYY."
        else:
            return day, month, year

    @staticmethod
    def date_convertor(parced):
        try:
            year = Date.date_validator(int(parced[2]), 9999)
            month = Date.date_validator(int(parced[1]), 12)
            day = Date.date_validator(int(parced[0]), dates.get(month) + int(month == 2 and year % 4 == 0))
        except:
            return [0, 0, 0]
        return day, month, year

    @staticmethod
    def date_validator(num, maximum):
        if num in range(1, maximum + 1):
            return num
        else:
            return 0


while True:
    d = Date(input("Введите дату в формате DD-MM-YYY, q - выход: "))
    if d.date == "q":
        break
    print(Date.date_parcer(d.date))

print("Конец программы")
