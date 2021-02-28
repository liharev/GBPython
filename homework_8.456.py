# Homework 8.4, 8.5 и 8.6
warehouse = []
class Warehouse():

    def __init__(self, name, space):
        self.name = name
        self.maxspace = space
        self.freespace = space
        self.equipment = {"Принтер": [0, 0], "Сканер": [0, 0], "Копир": [0, 0]}

    def printspacestatus(self, size, operation):
        print(f"Склад {self.name} {operation} {size} куб.м. Свободно {self.freespace} куб.м.")

    def addhw(self, accept):
        for hw in accept:
            if self.freespace < hw.size*accept[hw]:
                print("\033[91m {}\033[00m".format("Недостаточно места на складе! Используйте другой склад"))
                break
            self.equipment.get(hw.name)[0] += accept[hw]
            self.equipment.get(hw.name)[1] += hw.size*accept[hw]
            self.freespace -= hw.size*accept[hw]
            print(f"На склад {self.name} принят товар объемом {hw.size*accept[hw]} куб.м.")
            self.printspacestatus(hw.size*accept[hw], "получил")

    def subhw(self, delivery):
        for hw in delivery:
            if self.equipment.get(hw.name)[0] < delivery[hw]:
                print("\033[91m {}\033[00m".format("Недостаточно товара на складе!"))
                break
            self.equipment.get(hw.name)[0] -= delivery[hw]
            self.equipment.get(hw.name)[1] -= hw.size*delivery[hw]
            self.freespace += hw.size*delivery[hw]
            self.printspacestatus(hw.size*delivery[hw], "отгрузил")


class Hardware:
    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight

class Printer(Hardware):
    def __init__(self, size, weight, ptech):
        super().__init__("Принтер", size, weight)
        self.ptech = ptech

class Scanner(Hardware):
    def __init__(self, size, weight, dpi):
        super().__init__("Сканер", size, weight)
        self.dpi = dpi

class Copier(Hardware):
    def __init__(self, size, weight, ptech, dpi):
        super().__init__("Копир", size, weight)
        self.ptech = ptech
        self.dpi = dpi

print("\033[93m {}\033[00m".format("Создание складов!"))
while True:
    try:
        warehouse.append(Warehouse(input("\033[92m {}\033[00m".format("Введите название склада: ")), \
                                   int(input("\033[92m {}\033[00m".format("Введите объем хранения в куб.м.: ")))))
    except ValueError:
        continue
    i = input("Ввести новый склад - Y, иначе - продолжить: ")
    if i != "Y":
        break

print("\033[93m {}\033[00m".format("Создание типов оргтехники!"))
printer = Printer(0.25, 3, "ink")
scanner = Scanner(0.3, 2, 300)
copier = Copier(0.7, 10, "laser", 600)
print({printer.name: printer.size, scanner.name: scanner.size, copier.name: copier.size})

print("\033[93m {}\033[00m".format("Производим операции!"))
while True:
    operation = input("\033[92m {}\033[00m".format("Выберите операцию (1 - приход на склад, "
                                                         "2 - отгрузка со склада, q - выход): "))
    if operation == "q":
        break
    elif operation not in ("1", "2"):
        continue
    qty = input("\033[92m {}\033[00m".format("Введите через пробел количество перемещаемых принтеров, "
                                                   "сканеров и копиров: ")).split()
    try:
        i = 0
        for q in qty:
            i += 1
            q = int(q)
            if q < 0:
                raise ValueError
        if i != 3:
            raise ValueError
    except ValueError:
        print("\033[91m {}\033[00m".format("Ошибка ввода! Введите 3 целых неотрицательных числа!"))
        continue
    for wh in warehouse:
        print(f" {warehouse.index(wh)+1}.  {wh.name}: {wh.equipment}")
    if operation == "1":
        try:
            warehouse[int(input("\033[92m {}\033[00m".format("Введите номер склада прихода товара: ")))-1].\
                addhw({printer: int(qty[0]), scanner: int(qty[1]), copier: int(qty[2])})
        except:
            print("\033[91m {}\033[00m".format("Ошибка ввода!"))
            continue
    else:
        try:
            warehouse[int(input("\033[92m {}\033[00m".format("Введите номер склада отгрузки товара: ")))-1].\
                subhw({printer: int(qty[0]), scanner: int(qty[1]), copier: int(qty[2])})
        except:
            print("\033[91m {}\033[00m".format("Ошибка ввода!"))
            continue

print("Конец программы")