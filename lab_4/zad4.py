# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        return self.nazwa_produktu
    def ile_produktow(self):
        return str(self.ilosc) + self.jednostka_miary
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

zakupy = NaZakupy('pomidory', 2, 'kg', 4.99)

print(zakupy.wyswietl_produkt())
print(zakupy.ile_produktow())
print(zakupy.ile_kosztuje())