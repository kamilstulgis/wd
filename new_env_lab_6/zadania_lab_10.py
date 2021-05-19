import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
import random

iris = pd.read_csv('iris.data')
iris.columns = ['Szerokosc kielicha', 'Dlugosc kielicha', 'Szerokosc platka', 'Dlugosc platka', 'Rodzaj']
iris.to_csv('iris.data', index=False)

df = pd.read_excel('imiona.xlsx')

"""
Zadanie 1
Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).
"""
def zad_1():
    x = np.linspace(1, 20, 10)
    f_x = 1 / x
    # print(f_x)

# wykresy mogą być też dodawane do płótna definicja po definicji zamiast w pojedynczym wywołaniu funkcji plot()
# tutaj użyty został również parametr label, który określa etykietę danego wykresu w legendzie
    plt.plot(x, f_x, label='f(x) = 1/x')

    # # etykiety osi
    plt.xlabel('etykieta x')
    plt.ylabel('etykieta y')

    # # tytuł wykresu
    plt.title("Wykres funkcji f(x) dla x [1, 20]")

    # # włączamy pokazywanie legendy
    plt.legend()

    plt.show()
"""
Zadanie 2
Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
"""
def zad_2():
    x = np.linspace(1, 20, 10)
    f_x = 1 / x

    plt.plot(x, f_x, 'g>:', label='f(x) = 1/x')
    plt.xlabel('etykieta x')
    plt.ylabel('etykieta y')

    # # tytuł wykresu
    plt.title("Wykres funkcji f(x) dla x [1, 20]")

    # # włączamy pokazywanie legendy
    plt.legend()

    plt.show()

"""
Zadanie 3
Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.
"""
def zad_3():
    x = np.arange(0, 30, 0.1)
    s = np.sin(x)
    c = np.cos(x)

    plt.subplot(2, 1, 1)
    plt.plot(x, s, 'r-', label='sin(x)')

    plt.subplot(2, 1, 1)
    plt.plot(x, c, 'b:', label='cos(x)')
    plt.xlabel('x')
    plt.ylabel(' sin(x) / cos(x)')

    # # tytuł wykresu
    plt.title("Wykres sin(x) oraz cos(x) dla x [0, 30]")

    # # włączamy pokazywanie legendy
    plt.legend()

    plt.show()

"""
Zadanie 4
Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.
"""
def zad_4():
    x = np.arange(0, 30, 0.1)
    y = np.arange(0, 2, 2)
    s1 = (np.sin(x)*-1)-2
    s2 = np.sin(x)

    plt.subplot(2, 1, 1)
    plt.plot(x, s1, 'r-', label='sin(x)')

    plt.subplot(2, 1, 1)
    plt.plot(x, s2, 'b:', label='sin(x)')
    plt.xlabel('x')
    plt.ylabel(' sin(x)')

    # # tytuł wykresu
    plt.title("Wykres sin(x) oraz cos(x) dla x [0, 30]")

    # # włączamy pokazywanie legendy
    plt.legend()

    plt.show()
"""
Zadanie 5
Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y.
"""
def zad_5():
    # x = iris['Dlugosc kielicha']
    # y = iris['Szerokosc kielicha']
    # c = np.random.randint(0, 50, 150),
    data = {
        'x': iris['Dlugosc kielicha'],
        'y': iris['Szerokosc kielicha'],
        'c': np.random.randint(0, 50, 150),
        'z': 0
    }

    data['z'] = np.abs(data['x']-data['y'])

    plt.scatter('x', 'y', c='c', s='z', data=data)
    plt.xlabel('wartość sepal length')
    plt.ylabel('wartość sepal width')
    plt.show()

"""
Zadanie 6
Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.
"""
def zad_6():

    liczbaUrodzen = df.groupby(['Plec']).agg({'Liczba' : ['sum']})

    k = df.loc[df['Plec'] == 'K']
    m = df.loc[df['Plec'] == 'M']
    kSum = k.groupby(['Rok']).agg({'Liczba' : ['sum']})
    mSum = m.groupby(['Rok']).agg({'Liczba' : ['sum']})

    liczbaUrodzenZPodzialem = df.groupby(['Rok']).agg({'Liczba' : ['sum']})

    fig, ax = plt.subplots(nrows=1, ncols=3)

    wykres1 = liczbaUrodzen.plot.bar(subplots=True, ax=ax[0], xlabel='Płeć', ylabel='Liczba urodzeń')
    wykres2 = kSum.plot(subplots=True, ax=ax[1], color='red', xlabel='Rok', ylabel='Liczba urodzeń')
    mSum.plot(ax = wykres2, subplots=True,  color='green')

    wykres3 = liczbaUrodzenZPodzialem.plot.bar(subplots=True, ax=ax[2], color='orange', xlabel='Rok', ylabel='Liczba urodzeń')

    ax[0].legend(['Suma'])
    ax[0].set_title('Suma urodzeń z podziałem na płeć w latach 2000-2017')
    ax[1].legend(['Dziewczynki','Chłopcy'])
    ax[1].set_title('Suma urodzeń z podziałem na płeć w latach 2000-2017')
    ax[2].legend(['Suma'])
    ax[2].set_title('Suma urodzeń łącznie w latach 2000-2017')

    plt.show()

"""
Zadanie 7
Korzystając z tutoriala pod adresem https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596 lub innego zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast wykresu liniowego przedstawiał wykres łupkowy skumulowany (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków). Przykład:
"""
def zad_7():

    sumaKiM = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
    k = sumaKiM[sumaKiM['Plec'] == 'K']['Liczba']
    m = sumaKiM[sumaKiM['Plec'] == 'M']['Liczba']
    rok = df['Rok'].unique()

    plt.bar(rok, k, color='red', label='Dziewczynki')
    plt.bar(rok, m, color='green', label='Chłopcy', bottom=k)

    plt.show()

def zad_8(ile):

    list =[]
    for el in range(ile):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        list.append(x + y)

    plt.hist(list, facecolor='g')

    plt.xlabel('Wartości')
    plt.ylabel('Ilość rzutów')
    plt.title('Histogram')
    plt.grid('on')
    plt.show()

zad_1()
zad_2()
zad_3()
zad_4()
zad_5()
zad_6()
zad_7()
zad_8(12000)
# zad_9()
# zad_10()
