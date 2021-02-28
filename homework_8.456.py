# Homework 8.4
class warehouse():
    def __init__(self):
        pass

class hardware():
    def __init__(self, *args):
        pass

class printer(hardware):
    def __init__(self):
        pass

class scaner(hardware):
    def __init__(self):
        pass

class copier(hardware):
    def __init__(self):
        pass


class MyValueError(ValueError):
    def __init__(self, txt):
        print(txt)


print("Конец программы")