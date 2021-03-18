# Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9 wysokość=3
h = int(input("Podaj wysokość diamentu: "))
j = 1
k = h
if h >= 3 and h <= 9 and not(h%2==0):
    # liczba z przedzialu <3,9> i nie może być parzysta
    for i in range(1,h):
        print(' ' * k + 'o' * j + ' ' * k)
        # rysowanie w gore
        j +=2
        k -=1
        if j == h:
            print(' ' * k + 'o' * j + ' ' * k)
            # srodek diamentu
            for i in range(k,h):
                j -=2
                k +=1
                print(' ' * k + 'o' * j + ' ' * k)
                # rysowanie w dol
            break