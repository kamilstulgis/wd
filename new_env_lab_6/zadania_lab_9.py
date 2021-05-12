import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df = pd.read_excel('imiona.xlsx')
iris = pd.read_csv('iris.data')
iris.columns = ['Szerokosc kielicha', 'Dlugosc kielicha', 'Szerokosc platka', 'Dlugosc platka', 'Rodzaj']

"""
Zadanie 1
Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
"""
def zad_1():
     # print(df.groupby(['Rok']).agg({'Liczba': ['sum']}))
     grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
     wykres = grupa.plot()

     plt.xlim(2000,2017)
     wykres.set_ylabel('Liczba dzieci w tyś')
     wykres.set_xlabel('Rok')
     wykres.legend()

     plt.title('Populacja dzieci z podziałem na lata')
     plt.show()

"""
Zadanie 2
Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
"""
def zad_2():

     podzial = df.groupby(['Plec']).agg({'Liczba': ['sum']})
     # print(podzial)

     wykres = podzial.plot.bar()
     wykres.set_ylabel('Liczba dzieci w tyś')
     wykres.set_xlabel('Płeć')
     wykres.legend()

     plt.title('Populacja dzieci z podziałem na płeć')
     plt.show()
"""
Zadanie 3
Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
"""
def zad_3():

     data = df[(df['Rok'] >= 2013)]
     grupa = data.groupby(['Plec']).agg({'Liczba' : ['sum']})
     # print(grupa)

     wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
     plt.title('Liczba urodzony chłopców i dziewczynek, dane z ostatnich 5 lat')
     plt.show()

"""
Zadanie 4
Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego (scattered) wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie. Przykład można znaleźć w galerii wykresów biblioteki matplotlib - link w materiałach matplotlib."""
def zad_4():

     a = iris['Szerokosc platka'][(iris['Rodzaj'] == 'Iris-versicolor')]
     b = iris['Dlugosc platka'][(iris['Rodzaj'] == 'Iris-versicolor')]
     plt.scatter(a, b, color = 'red')

     c = iris['Szerokosc platka'][(iris['Rodzaj'] == 'Iris-virginica')]
     d = iris['Dlugosc platka'][(iris['Rodzaj'] == 'Iris-virginica')]
     plt.scatter(c, d, color = 'blue')

     e = iris['Szerokosc platka'][(iris['Rodzaj'] == 'Iris-setosa')]
     f = iris['Dlugosc platka'][(iris['Rodzaj'] == 'Iris-setosa')]
     plt.scatter(e, f, color = 'green')

     plt.show()

"""
Zadanie 5
Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv)."""
def zad_5():

     data = pd.read_csv('zamowienia.csv', delimiter=';')
     podzial = data.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})

     wykres = podzial.plot.bar()
     wykres.set_ylabel('Liczba zamówień')
     wykres.set_xlabel('Sprzedawca')
     wykres.legend()

     plt.title('Zamówienia z podziałem na sprzedawców')
     plt.show()

zad_1()
zad_2()
zad_3()
zad_4()
zad_5()