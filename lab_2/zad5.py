import sys

a= int(input("Podaj 1 liczbe: "))
b= int(input("Podaj 2 liczbe: "))
c= int(input("Podaj 3 liczbe: "))
if (a > -1 and a < 11) and (a > b or b > c):
    print('Warunki spełnione 😻 ')
else:
    print('warunki niespełnione 😥')