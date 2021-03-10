# imie='Ala ma kota'
# a=7
# a+=2
# print(imie)
# print(a)
# print(type(a))
# print(1/2)
# suma = 1+2*4/4
# print(suma)
# print(type(suma))
# reszta =12%5
# print(reszta)
# potega = 5 ** 3
# print(potega)
# full_name ='Kamil ' + 'Stulgis'
# print(full_name)
# spam = 'spam '*10
# print(spam)
# prawda = True
# falsz = False
# print(bool(prawda and falsz))
# liczba = 1
# liczba2 = liczba
# print(liczba is liczba2)
# print(liczba is not liczba2)
# lista = [1, 2, 5, 8]
# print(1 in lista)
# print(4 is not lista)
import math as m

# e=2
# print(m.pow(e,10))
# print(m.sqrt((m.log(5+m.sin(8)**2))))
# print(m.floor(3.55))
# print(m.ceil(4.80))

# # print(dir(__builtins__))

# name ='KAMIL'
# surname ='STULGIS'
# full_name = name.capitalize()+ ' ' + surname.capitalize()
# print(full_name)

# text = "la la la la koko dżambo la la do przodu".count('la')
# print(text)

# proffession = 'Plumber'
# print(proffession[1], proffession[-1])

# lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

# print(lorem.split())

# name2='Kamil'
# surname2="Stulgis"
# litera_1=name2[1]
# litera_2=surname2[2]
# example='Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza'

# n=example.count(litera_1)
# s=example.count(litera_2)
# paragraph='W tekscie jest liczba' ,n, 'liter' ,litera_1, 'oraz liczba' ,s, 'liter' ,litera_2

# print(paragraph)

# wd 2
import sys
# a = input("Tu jest jakiś komunikat np. Podaj liczbę\n")
# print(a)

# print("Podaj jakiś tekst")
# s = sys.stdin.readline() #Wczytuje wiersz
# print("Twój tekst to: " + s)
# Do wydruku można użyć też komendy write np.
# sys.stdout.write(s)

# zad 1
# a = input('Wprowadź swoje zdanie: \n')
# s = a.count(' ')
# print(s)

# zad 2
# print('Podaj pierwsza liczbe: \n')
# x = sys.stdin.readline()
# print('Podaj druga liczbe: \n')
# y = sys.stdin.readline()
# z = int(x)*int(y)
# sys.stdout.write(str(z))

# x =int(input('Podaj liczbe: '))
# y =int(input('Podaj druga liczbe: '))
# z = x*y
# sys.stdout.write(str(z))

# zad 4
# x = int(input('Podaj liczbe: '))

# if x > 0:
#     print('Wartość bezwgledne Twojej liczby wynosi ' + str(x))
# elif x < 0:
#     print('Wartość bezwględna Twojej liczb wynosi ' + str(x*-1))
# else:
#     print('Wartość bezwględne Twojej liczby jest równa ' + str(x))

# zad 5
# a= int(input("Podaj 1 liczbe: "))
# b= int(input("Podaj 2 liczbe: "))
# c= int(input("Podaj 3 liczbe: "))
# if (a > -1 and a < 11) and (a > b or b > c):
#     print('Warunki spełnione 😻 ')
# else:
#     print('warunki niespełnione 😥')

