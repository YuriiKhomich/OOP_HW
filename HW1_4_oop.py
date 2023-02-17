# Task 4  Зробити можливим передавати температуру та шкалу в метод з п.2


class ChemicalElement():
    def __init__(self, melt, boilt):
        self.melt = melt
        self.boilt = boilt
    def temperature(self, temp, sys_t):
        temp = self.temp_calc(temp, sys_t)
        if temp >= self.melt and temp < self.boilt:
            return "Substance to melt"
        elif temp >= self.boilt:
            return 'Matter boils'
    def temp_calc(self, temp, sys_t):
        if sys_t == "K":
            return temp - 273,15
        elif sys_t == "F":
            return (temp-32)*5/9
        else:
            return temp
bomm = ChemicalElement(1000,2000)
print (bomm.temperature(2200,"F"))
print (bomm.temp_calc(2200,"F"))