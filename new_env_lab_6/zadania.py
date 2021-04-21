import numpy as np
import sys

"""Zadanie 1
Za pomocą funkcji arange stwórz tablicę Numpy składającą się 20 kolejnych wielokrotności liczby 2."""

a = np.arange(0,40,2)
print (a)


"""Zadanie 2
Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64."""
b = np.array([1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.2])
c = b.astype('int64')
print(c)
print(c.dtype)

"""Zadanie 3
Napisz funkcję, która będzie:

przyjmowała jeden parametr n w postaci liczby całkowitej
zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1"""

def nr(n):
    if type(n) == int:
        a = np.arange(1,n*n+1).reshape(n,n)
        print(a)
nr(4)
nr(5)
nr(3)

"""Zadanie 4
Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2 4 8 16]"""

def do_potegi(potega,ilosc_poteg):
    a = np.logspace(1, ilosc_poteg, num=ilosc_poteg, base=potega)
    print(a)
do_potegi(2,4)
do_potegi(2,3)
do_potegi(3,4)

""" Zadanie 5
Napisz funkcję, która:

na wejściu przyjmuje jeden parametr określający długość wektora,
na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
generuje macierz diagonalną z w/w wektorem jako przekątną"""

def macierz(dlugosc_wektora):
    rev = np.arange(dlugosc_wektora+1)
    print(rev[dlugosc_wektora:0:-1])
    mat_diag = np.diag([dlugosc_wektora for x in range(5)])
    print(mat_diag)
macierz(3)
macierz(8)

"""Zadanie 6
Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej."""

marcin = 'MxxxxxAAxxxxRxLxxxCxxAxxIxxxRxNODROZ'
mar_1 = np.array(list(marcin))
print(mar_1.reshape(6,6))

kamil = 'kamil'
baton = 'baton'
rower = 'rower'

def wykreslanka(n,slowo_pionowe, slowo_skos,slowo_odwrocone):

    tablica = np.ones((n,n), dtype='U1')

    for x in range(len(kamil)):
        tablica[x,0] = kamil[x]

    for y in range(len(baton)):
        tablica[y,y+1] = baton[y]

    licznik=0
    for z in range(len(rower),0,-1):
        tablica[5,licznik] = rower[z-1]
        licznik+=1

    return tablica

# print(wykreslanka(6,'kamil','baton','rower'))

"""Zadanie 7
Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:"""

"""[2 4 6] 8
   [4 2 4] 6
   [6 4 2] 4"""
""" 8 6 4  2 """
"""Przy założeniach:
funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej."""

def rysuje(n):
    licznik = 2

    z = np.empty((n,n), dtype='int64')
    for x in range(0,3,1):
        for y in range(0,3,1):
            z[y,x] = licznik
            z[x,y] = licznik
            z[x,x] = 2
        licznik+=2
    return z

"""Zadanie 8
Napisz funkcję, która:
jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)"""

def tablica_dzielona(tablica,kierunek):
    if kierunek == 'pionowo':
        if tablica.shape[0] % 2 == 0:
            newarr= np.hsplit(tablica,2)
            print(newarr)
        else:
            print('Nieparzysta liczba kolumn')
    elif kierunek == 'poziomo':
        if tablica.shape[0] % 2 == 0:
            newarr = np.vsplit(tablica,2)
            print(newarr)
        else:
            print('Nieparzysta liczba wierszy')
    else:
        return 'błędne dane'

print(tablica_dzielona(np.arange(16).reshape((4,4)), 'pionowo'))
print(tablica_dzielona(np.arange(16).reshape((4,4)), 'poziomo'))

"""Zadanie 9
Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego."""

fibo = np.empty((5,5), dtype='int64')
n1=0
n2=1
suma = n1 + n2
for x in range(0,5):
    for y in range(0,5):
        fibo[x,y] = suma
        n1 = n2
        n2 = suma
        suma = n1 + n2
print(fibo)