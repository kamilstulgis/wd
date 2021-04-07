# Poczytaj o metodach __ge__, __gt__, __le__, __lt__, przeciąż je i spróbuj wykorzystać w instrukcji warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.

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

    def __ge__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x >= kwadrat.x
        else:
            return 'błędne dane'

    def __gt__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x > kwadrat.x
        else:
            return 'błędne dane'

    def __le__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x <= kwadrat.x
        else:
            return 'błędne dane'

    def __lt__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x < kwadrat.x
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
print(kw2 >= kw)
print(kw2 <= kw)
print(kw2 > kw)
print(kw2 < kw)