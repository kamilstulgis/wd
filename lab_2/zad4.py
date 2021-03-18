import sys

x = int(input('Podaj liczbe: '))

if x > 0:
    print('Wartość bezwgledne Twojej liczby wynosi ' + str(x))
elif x < 0:
    print('Wartość bezwględna Twojej liczb wynosi ' + str(x*-1))
else:
    print('Wartość bezwględne Twojej liczby jest równa ' + str(x))