import sys

lista=[]
licznik = 1
while  licznik > 0:
    x = int(input('Podaj liczbe: '))
    lista.append(x)
    y = int(input('Wprowadź 0 jeśli chcesz zakończyć: '))
    if y == 0:
        licznik = 0
    else:
        licznik = 1
print(f'Twoje liczby to {lista}')