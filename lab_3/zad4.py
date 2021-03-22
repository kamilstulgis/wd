# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = a x + b

def liniowa(a, x, b):
    y = a * x + b
    if a > 0:
        return 'Funkcja jest rosnąca'
    elif a < 0:
        return 'Funkcja jest malejąca'
    elif a == 0:
        return 'funkcja jest stała'
    else:
        return 'Podałeś błędne dane'

print(liniowa(0, 1, 0))
print(liniowa(-1, 5, -2))
print(liniowa(2, 4, 3))