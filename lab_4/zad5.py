# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.
import math

class Ciag:
    def __init__(self, start, r, ile):
        self.start = start
        self.r = r
        self.ile = ile

    def wyswietl_dane(self):
        dane = [self.start, self.r, self.ile]
        return dane

    def pobierz_elementy(self, ciag):
        self.ciag = ciag
        return ciag

    def pobierz_parametry(self, start, r, ile):
        ciag_wypisz = [x for x in range(start, ile*r+start, r)]
        return ciag_wypisz

    def policz_sume(self):
        return sum(self.pobierz_elementy(self.ciag))

    def policz_elementy(self):
        roznica = self.ciag[1] - self.ciag[0]
        if roznica > 0 or roznica < 0:
            elementy = len(self.ciag)
        return elementy

ciag = Ciag(1,2,10)

print(ciag.wyswietl_dane())
print(ciag.pobierz_elementy([-1,-2]))
print(ciag.pobierz_parametry(1,1,10))
print(ciag.policz_sume())
print(ciag.policz_elementy())