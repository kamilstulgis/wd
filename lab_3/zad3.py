# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

# Mechanizm przedstawiony w tym podrozdziale jest bardzo przydatny, chociaż skomplikowane polecenia mogą być wyzwaniem do zinterpretowania względem „tradycyjnego” podejścia. Więcej przykładów można znaleźć w dokumentacji Pythona pod adresem https://docs.python.org/3.8/tutorial/datastructures.html#nested-list-comprehensions

produkty = {'pomidory': 'kilogramy',
'koperty': 'sztuki',
'cukier': 'kilogramy',
'telefony': 'sztuki'}

odwrocone = {value:key for key, value in produkty.items()}
print(odwrocone)
sztuki = {odwrocone['sztuki'] for x in odwrocone}
print(list(sztuki))

# szt = [odwrocone['sztuki'] for key in odwrocone.keys()]
# print(szt)
