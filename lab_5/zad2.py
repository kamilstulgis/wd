# Przeciąż metodę __add__() dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat o nowym boku, będącym sumą boków dodawanych do siebie kwadratów.

class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x + kwadrat.x
        else:
            return 'błędne dane'

kw = Kwadrat(1)
kw1 = Kwadrat(2)
kw2 = Kwadrat(3)
kw3 = Kwadrat(4)
kw4 = Kwadrat(5)
print(kw + 1)
print(kw2 + kw3)
print(kw1 + kw2)
print(kw3 + kw4)