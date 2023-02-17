# Task 3 Додати в клас метод, який приймає в якості аргументів температуру (число)
# та назву шкали виміру (“C” / “F” / “K”) та конвертує її в градуси цельсія.

class ChemicalElement():
    def __init__(self, melt, boilt):
        self.melt = melt
        self.boilt = boilt

    def temperature(self, temp):
        if temp >= self.melt and temp < self.boilt:
            return "Substance to melt"
        elif temp >= self.boilt:
            return "Matter boils"

    def temp_calc(self, temp, sys_t):
        if sys_t == "K":
            return temp - 273, 15
        elif sys_t == "F":
            return (temp - 32) * 5 / 9
        else:
            return temp


bomm = ChemicalElement(1000, 2000)
print(bomm.temperature(2273.15))
print(bomm.temp_calc(1500, "F"))
