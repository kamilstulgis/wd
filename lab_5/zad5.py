# Za pomocą funkcji isinstance() oraz issubclass() sprawdź wynik dla instancji obiektu Pracownik oraz Menadzer dla klas Osoba, Pracownik i Manadzer.

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())
print('-------------')
x = issubclass(Pracownik, Menadzer)
y = issubclass(Menadzer, Pracownik)
z = issubclass(Menadzer, Osoba)
print(x)
print(y)
print(z)
print('-------------')
a = isinstance(jozek, Pracownik)
print(a)
b = isinstance(adrian, Menadzer)
print(b)
c = isinstance(jozek, Menadzer)
print(c)