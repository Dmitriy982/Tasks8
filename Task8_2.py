class OwnError(Exception):
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ex(self):
        try:
            nn = int(self.n)
            mm = int(self.m)
            print(nn / mm)
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)


f = OwnError(input("Введите первое число: "), input("Введите второе число: "))
f.ex()

