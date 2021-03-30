# Stwórz klasę Robot, która będzie sterować ruchami robota. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla robota), i powinna mieć następujące metody:

# konstruktor – który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne robota
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody.

class Robot:
    def __init__(self, x, y, krok = 1):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self,ile_krokow):
        if ile_krokow > 0:
            self.y += ile_krokow
            return (f'Poruszyłeś się o {ile_krokow} kroków w górę')
        else:
            return 'Podałeś błędne dane'

    def idz_w_dol(self,ile_krokow):
        if ile_krokow > 0:
            self.y -= ile_krokow
            return (f'Poruszyłeś się o {ile_krokow} kroków w dół')
        else:
            return 'Podałeś błędne dane'

    def idz_w_lewo(self,ile_krokow):
        if ile_krokow > 0:
            self.x -= ile_krokow
            return (f'Poruszyłeś się o {ile_krokow} kroków w lewo')
        else:
            return 'Podałeś błędne dane'

    def idz_w_prawo(self, ile_krokow):
        if ile_krokow > 0:
            self.x += ile_krokow
            return (f'Poruszyłeś się o {ile_krokow} kroków w prawo')
        else:
            return 'Podałeś błędne dane'

    def pokaz_gdzie_jestes(self):
        return (f'Twoje aktualne współrzędne to ({self.x},{self.y})')

    def __del__(self):
        print('Instancja obiektu została zniszczona')


alex = Robot(0,0)
print(alex.pokaz_gdzie_jestes())
print(alex.idz_w_gore(5))
print(alex.idz_w_dol(10))
print(alex.idz_w_lewo(4))
print(alex.idz_w_prawo(10))
print(alex.pokaz_gdzie_jestes())
del alex