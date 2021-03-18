# Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów
# oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).
person = {'first': 'Jean-Luc', 'last': 'Picard'}

print('{:^10}'.format('test'))
print('{:d}'.format(-98))
print('{:f}'.format(3.141592653589793))
print('{:4d}'.format(32))
print('{:=+5d}'.format(23))
print('{first} {last}'.format(first='Hodor', last='Hodor!'))
print('{p[first]} {p[last]}'.format(p=person))