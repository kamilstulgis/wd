# Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego. Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa), r (wielkość o ile rosną kolejne elementy) i ile_elementów (ile elementów ma sumować). Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.

def ciag(a1= 1, r=2, ile=3):
    i = 0
    if ile == 0:
        return 0.0
    else:
        suma = 0.0
    while i < ile:
        suma += a1
        print(a1)
        a1 += r
        i += 1
    return suma

print(ciag())
print(ciag(2,3,4))
print(ciag(6,2,3))
print(ciag(1,1,1))
print(ciag(-2,-1,5))


# 2 rozwiazanie

def suma(a1= 1, r=5, ile=3):
    wynik=0
    y=a1
    for x in range(a1, ile+1):
        wynik +=y
        y +=r

    return wynik

print(suma())

