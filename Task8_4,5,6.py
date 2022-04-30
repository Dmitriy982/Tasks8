class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Название {self.name} цена: {self.price}"

    def store(self):
        try:
            n = int(self.price)
        except ValueError:
            return "Неверные данные"
        else:
            return {self.name: n}


class Printer(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)


class Scanner(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)


class Xerox(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)


p_1 = Printer("Print", "1400")
p_2 = Scanner("Scan", "2600")
p_3 = Xerox("Xer", "3800")
print(p_1)
print(Equipment.store(p_1))
print(p_2)
print(Equipment.store(p_2))
print(p_3)
print(Equipment.store(p_3))
