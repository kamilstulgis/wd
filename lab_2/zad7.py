import sys

lista = []
nr = int(input('Podaj liczbe ile razy ma się wykonać pętla: '))
for i in range(0, nr, 1):
    x = int(input('Podaj liczbe: '))
    lista.append((pow(x, 2)))
print(lista)