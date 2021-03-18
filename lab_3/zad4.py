def liniowa(a, b):
    if a > 0:
        return 'Funkcja jest rosnąca'
    elif a < 0:
        return 'Funkcja jest malejąca'
    elif a == 0:
        return 'funkcja jest stała'
    else:
        return 'Podałeś błędne dane'

print(liniowa(0,0))
print(liniowa(-1,-2))
print(liniowa(2,3))