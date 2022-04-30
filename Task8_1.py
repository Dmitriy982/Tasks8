class Date:
    def __init__(self, da, mo, ye):
        self.da = da
        self.mo = mo
        self.ye = ye

    @staticmethod
    def get_date(obj):
        if 31 >= obj.da >= 1 and 12 >= obj.mo >= 1 and 2022 >= obj.ye >= 1990:
            return f"{obj.da} {obj.mo} {obj.ye}"
        else:
            return "Неправильные данные"

    @classmethod
    def set_date(cls, date):
        d, m, y = date
        return cls(int(d), int(m), int(y))


m_list = ["30", "1", "1998"]
first = Date.set_date(m_list)
print(Date.get_date(first))



