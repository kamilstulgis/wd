# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa:
    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2
# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
    def sprawdz_czy_palindrom(self,slowo1):
        slowo2 = slowo1[::-1]
        if slowo1 == slowo2:
            return 'Podane slowo jest palindromem'

        return 'Podane slowo nie jest palindromem'

# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
    def sprawdz_czy_metagramy(self, slowo1,slowo2):
        list1 = list(slowo1)
        list2 = list(slowo2)
        list3=[]
        if len(list1) == len(list2):
            for x in range(len(list1)):
                if list1[x] != list2[x]:
                    list3.append(list2[x])
            if len(list3) == 1:
                return 'Podane słowa są metagramami'
            else:
                return 'Podane słowa nie są metagramami'
        else:
            return 'Podane słowa nie są metagramami'

    def sprawdz_czy_anagramy(self, slowo1, slowo2):
        list1 = sorted(list(slowo1))
        list2 = sorted(list(slowo2))
        if len(list1) == len(list2):
            for x in range(len(list1)):
                if list1[x] != list2[x]:
                    return 'nie są'
        return "są"

    def wyświetl_wyrazy(self, slowo1,slowo2):
        return slowo1, slowo2

wyraz = Slowa('kajak', 'zmmija')



print(wyraz.sprawdz_czy_palindrom('kajak'))
print(wyraz.sprawdz_czy_palindrom('zmija'))
print(wyraz.sprawdz_czy_metagramy('kajak', 'kajak'))
print(wyraz.sprawdz_czy_metagramy('pada','kada'))
print(wyraz.sprawdz_czy_anagramy('pada','kada'))
print(wyraz.sprawdz_czy_anagramy('mata','tama'))
print(wyraz.wyświetl_wyrazy('andrzej','wróbel'))