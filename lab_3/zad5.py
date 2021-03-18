def prosta(a1, b1, a2, b2):
    if a1 == a2:
        return 'Proste są równoległe'
    elif a1*a2 == -1:
        return 'Proste są prostopadłe'
    else:
        return 'Podana błedne dane'
print(prosta(1,1,1,1))
print(prosta(1,1,-1,1))

