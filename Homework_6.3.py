# Homework 6.3

class Worker:
    def __init__(self) -> object:
        self.__income = {}
        self.name = input("Введите имя сотрудника: ")
        self.surname = input("Введите имя сотрудника: ")
        self.position = input(f"Введите должность {self.name + ' ' + self.surname}: ")
        self.__income.update({"wage": input(f"Введите оклад {self.name + ' ' + self.surname}: ")})
        self.__income.update({"bonus": input(f"Введите премию {self.name + ' ' + self.surname}: ")})
    def get_wage(self):
        return int(self.__income.get("wage"))
    def get_bonus(self):
        return int(self.__income.get("bonus"))

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self.get_wage()+self.get_bonus()
p = []
count = 0
while input("Нажмите любую клавишу, q - выход: ") != "q":
    p.append(Position())
    print(f"Полное имя: {p[count].get_full_name()}")
    print(f"Оклад + премия: {p[count].get_total_income()}")
    count += 1

print("Конец программы!")