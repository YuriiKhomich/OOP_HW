#Task 1. Для класу має бути описаний метод __init__(...), який приймає два параметри:
#температура плавлення та температура кипіння.
#Task 2. В класі має бути описаний метод, який в якості аргумента отримує температуру
#(в градусах цельсія) та повертає строку, яка відповідає агрегатному стану речовини при цій температурі.

class ChemicalElement():
    def __init__(self, melt, boilt):
        self.melt = melt
        self.boilt = boilt
    def temperature(self, temp):
        if temp >= self.melt and temp < self.boilt:
            return "Substance to melt"
        elif temp >= self.boilt:
            return "Matter boils"
bomm = ChemicalElement(100,200)
print (bomm.temperature(120))

