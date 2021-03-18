import sys

liczba = range(0,50)
lista = []
for i in liczba:
    if i % 5 == 0:
        lista.append(i)
print(lista)