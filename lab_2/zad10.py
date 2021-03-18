import sys

licznik = input('Podaj wysokość wieży: ')
i = 1

if int(licznik) < 11 and int(licznik) > 0:
    print('działa')
    while i <= int(licznik):
        sys.stdout.write('A'* i)
        sys.stdout.write('\n')
        i+=1
else:
    print('Podano błędną wartość')