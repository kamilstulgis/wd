# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
import sys

print('Podaj kierunek studiów, rok i specjalność')
dane = sys.stdin.readline()
print('Podaj imie')
name = sys.stdin.readline()
print('Podaj nazwisko')
surname = sys.stdin.readline()
print('Podaj nr telefonu')
nr = sys.stdin.readline()

lista = [dane, name, surname, nr]
with open('lab4_zad1.txt', 'a+') as plik:
    plik.write(dane)
    plik.writelines(lista)

print('#####################')

with open('lab4_zad1.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')