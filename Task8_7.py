class Comp:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return f"({self.num[0] + other.num[0]} {self.num[1] + other.num[1]}j)"

    def __str__(self):
        return str(self.num)

    def __mul__(self, other):
        return f"({self.num[0] * other.num[0] - self.num[1] * other.num[1]} {self.num[0] * other.num[1] + self.num[1] * other.num[0]}j)"


c1 = Comp([3, 1])
c2 = Comp([2, -3])
print(c1 + c2)
print(c1 * c2)
print("____________Проверка_______________")
print(complex(3, 1) + complex(2, -3))
print(complex(3, 1) * complex(2, -3))

