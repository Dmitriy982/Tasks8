class OwnError(Exception):
    @staticmethod
    def ex():
        s = 1
        list2 = []
        while s > 0:
            list1 = (input("Введите числа через пробел или q для выхода: "))
            if list1 == "q":
                s = 0
                print(list2)
            elif not list1.isdigit():
                print("Это не число: ")
            else:
                list2.append(list1)
                print(list2)


OwnError.ex()
