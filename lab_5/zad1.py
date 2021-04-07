# class Ksztalty:
#     # definicja konstruktora
#     def __init__(self, x, y):
#         # deklarujemy atrybuty
#         # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
#         self.x=x
#         self.y=y
#         self.opis = "To będzie klasa dla ogólnych kształtów"

#     def pole(self):
#         return self.x * self.y

#     def obwod(self):
#         return 2 * self.x + 2 * self.y

#     def dodaj_opis(self, text):
#         self.opis = text

#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.x = self.y * czynnik


# # a teraz klasa która dziedziczy po klasie Ksztalty
# class Kwadrat(Ksztalty):

#     def __init__(self, x):
#         self.x =x
#         self.y=x

# # i jeszcze klasa, która dziedziczy po klasie Kwadrat
# # bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
# #  _
# # | |_
# # |_ _|
# class KwadratowaLiteraL(Kwadrat):

#     def obwod(self):
#         return 8 * self.x

#     def pole(self):
#         return 3 * self.x * self.y

# print("inicjujemy klasę Kwadrat")
# figura = Kwadrat(5)

# # sprawdzamy metody z klasy bazowej
# print(figura.pole())

# print(figura.obwod())

# figura.dodaj_opis("Kwadrat")

# print(figura.opis)

# figura.skalowanie(0.3)

# print(figura.obwod())

# print("inicjujemy klasę KwadratowaLiteraL")
# litera_l = KwadratowaLiteraL(5)

# # sprawdzamy jakie możemy wywołać metody
# print(litera_l.obwod())
# print(litera_l.pole())
# litera_l.dodaj_opis("Litera L")
# print(litera_l.opis)
# litera_l.skalowanie(0.5)
# print(litera_l.obwod())

# Stwórz 3 klasy: Material, Ubrania, Sweter. Klasa: Material

# Atrybuty:

# rodzaj,
# długość
# szerokość
# Metody:

# konstruktor
# wyświetl_nazwę
# Klasa: Ubrania

# Atrybuty:

# rozmiar
# kolor
# dla_kogo
# Metody:

# wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter

# Atrybuty:

# rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:

# wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.

class Material:
    def __init__(self, rodzaj ='Jedwab', dlugosc ='600cm', szerokosc='800cm'):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.nazwa = 'nazwa'

    def wyswietl_nazwe(self,tekst):
        self.nazwa = tekst
        return (f'Nazwa: {self.nazwa}')

class Ubrania(Material):
    rozmiar = 'S'
    kolor = 'czarny'
    dla_kogo = "kobieta"

    def wyswietl_dane(self):
        return (f'Ubranie: {self.rozmiar}, {self.kolor}, {self.dla_kogo}')

class Sweter(Ubrania):
    rodzaj_swetra = 'rozpinany'

    def wyswietl_dane(self):
        return (f'Rodzaj swetra: {self.rodzaj_swetra}')

mate = Material('Len', 300, 100)
print(mate.wyswietl_nazwe('tekst'))
ubr = Ubrania()
swe = Sweter()

print(swe.wyswietl_nazwe('len'))
print(swe.rozmiar)
print(ubr.wyswietl_dane())
print(swe.wyswietl_dane())
print(ubr.dla_kogo)
ubr.dla_kogo = 'dziecko'
print(ubr.dla_kogo)
swe.rodzaj_swetra = 'z golfem'
print(swe.wyswietl_dane())
print(swe.rodzaj)
swe.rodzaj = 'len'
print(swe.rodzaj)



# class Ksztalty:
#     # definicja konstruktora
#     def __init__(self, x, y):
#         # deklarujemy atrybuty
#         # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
#         self.x=x
#         self.y=y
#         self.opis = "To będzie klasa dla ogólnych kształtów"

#     def pole(self):
#         return self.x * self.y

#     def obwod(self):
#         return 2 * self.x + 2 * self.y

#     def dodaj_opis(self, text):
#         self.opis = text

#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.x = self.y * czynnik

# class Kwadrat(Ksztalty):

#     def __init__(self, x):
#         self.x = x
#         self.y = x
#     def __add__(self):
#         return self.x + self.y

#     def __str__(self):
#         return 'Kwadrat o boku {}'.format(self.x)

# kw = Kwadrat(5)
# print(kw)
# kw1 = Kwadrat(2)
# kw2 = Kwadrat(6)
# kw3 = Kwadrat(5)
# kw4 = Kwadrat(1)
# kw5 = Kwadrat(4)

# print(kw.__add__())
# print(kw1.__add__())
# print(kw2.__add__())
# print(kw3.__add__())
# print(kw4.__add__())
# print(kw5.__add__())
