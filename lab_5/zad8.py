# Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego. Zaimplementuj sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora (sprawdź funkcję isinstance()).

class Samogloski:
    def __init__(self, tekst):
        if isinstance(tekst, str):
            self.tekst = tekst
            self.letters = [letter for letter in self.tekst]
            self.index = -1
            self.dlugosc = len(self.tekst)
            self.lista_samoglosek = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
        else:
            return 'brak samogłosek'

    def __iter__(self):
        return self

    def __next__(self):

        if self.dlugosc <= self.index:
            raise StopIteration
        for letter in range(self.index, self.dlugosc-1):
            self.index += 1
            if self.tekst[self.index] in self.lista_samoglosek:
                return self.tekst[self.index]
        else:
            return 'brak samogłosek'


tekst = Samogloski('yeti, o, jarząbina')

print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))