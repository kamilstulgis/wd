# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami:
# y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1

def prosta(a1, b1, x1, a2, b2, x2):
    y1 = a1 * x1 + b1
    y2 = a2 * x2 + b2
    if a1 == a2:
        return 'Proste są równoległe'
    elif a1*a2 == -1:
        return 'Proste są prostopadłe'
    else:
        return 'Podana błedne dane'
print(prosta(1, 1, 2, 1, 1, 1))
print(prosta(1, 1, -2, -1, 1, -3))