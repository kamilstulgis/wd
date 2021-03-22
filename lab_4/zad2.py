# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.

plik = open('lab4_zad1.txt', 'r')
linia = plik.readline()
plik.close()
print(linia)

with open('lab4_zad1.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')