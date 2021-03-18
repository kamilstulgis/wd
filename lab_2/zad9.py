import sys

liczba =input("Podaj swoją liczbę: ")
i = 0
suma = 0
while i < len(liczba):
    suma += int(liczba[i])
    i +=1
else:
    print(suma)