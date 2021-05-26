import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


"""
Zadanie 1
Wygeneruj wykres liniowy dla z od 0 do 2pi, x = sin(z), y = 2cos(z).
"""
def zad_1():
    fig = plt.figure(figsize=(10,5))
    ax = fig.gca(projection = '3d')

    z = np.linspace(0, 2 * np.pi)
    x = np.sin(z)
    y = 2 * np.cos(z)
    ax.plot(x, y, z, label = 'zadanie 1')
    ax.legend()
    plt.show()

"""
Zadanie 2
Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i kolorów: https://matplotlib.org/api/markers_api.html
"""
def zad_2():
    np.random.seed( 19680801 )

    def randrange(n, vmin, vmax):
        '''
        Funkcja wspomagająca może tworzyć macierz losowych liczb o
        kształcie(n, )
        '''
        return (vmax - vmin)*np.random.rand(n) + vmin


    fig = plt.figure()
    ax = fig.add_subplot(111 , projection = '3d')
    n = 10

    # Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
    # zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ( 'b', '^', -10, -5), ( 'g', 'v', -80, -20), ( 'c', 's', -40, -15), ( 'y', '+', -50, -15)]:
        x1 = randrange(n, 23, 32)
        x2 = randrange(n, 0, 100)
        x3 = randrange(n, 15, 60)
        x4 = randrange(n, 50, 80)
        x5 = randrange(n, 5, 10)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(x1, x2, zs, c=c, marker=m)
        ax.scatter(x3, x4, x5, zs, c=c, marker=m)


    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

"""
Zadanie 3
Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach: https://matplotlib.org/examples/color/colormaps_reference.html
"""

def zad_3():
    color = [cm.hot, cm.cool, cm.copper, cm.binary, cm.bone, cm.brg, cm.flag, cm.ocean, cm.jet]

    for n in range(5):
        col = np.random.choice(color,1)
        print(col[0])
        fig = plt.figure()
        ax = fig.gca(projection = '3d')
        # generuj dane.
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)
        # rysuj powierzchnię.
        surf = ax.plot_surface(X, Y, Z, cmap = col[0],
        linewidth = 0 , antialiased = False)
        ax.set_zlim(-1.01 , 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        # Dodanie paska kolorów.
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

"""
Zadanie 4
Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.
"""

def zad_4():

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(151, projection = '3d')
    ax2 = fig.add_subplot(152, projection = '3d')
    ax3 = fig.add_subplot(153, projection = '3d')
    ax4 = fig.add_subplot(154, projection = '3d')
    ax5 = fig.add_subplot(155, projection = '3d')
    # fikcyjne dane
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bot = x-y
    bottom = np.zeros_like(top)
    height = bottom = np.zeros_like(bot)

    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
    ax1.set_title('Wykres zacieniony')
    ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
    ax2.set_title('Wykres nie zacieniony')
    ax3.bar3d(x, y, height, width, depth, bot, shade = True )
    ax3.set_title('Wykres 3')
    ax4.bar3d(x, y, height, width, depth, bot, shade = False )
    ax4.set_title('Wykres 4')
    ax5.bar3d(x, y, bottom, width, depth, top, shade = True )
    ax5.set_title('Wykres 5')
    plt.show()

"""
Zadanie 5
W przykładzie 3 zmień gęstość próbek do wykresu na krok 0.1 oraz włącz antyaliasing. Wyświetl pierwotny i nowy wykres obok siebie.
"""
def zad_5():
    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121, projection = '3d')
    ax2 = fig.add_subplot(122, projection = '3d')
    # generuj dane.
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    # rysuj powierzchnię.
    surf1 = ax1.plot_surface(X, Y, Z, cmap =cm.coolwarm,
    linewidth = 0 , antialiased = True)
    ax1.set_zlim(-1.01 , 1.01)
    ax1.zaxis.set_major_locator(LinearLocator(10))
    ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    A = np.arange(-5, 5, 0.25)
    B = np.arange(-5, 5, 0.25)
    A, B = np.meshgrid(A, B)
    C = np.sqrt(A ** 2 + B ** 2)
    D = np.sin(C)
    # rysuj powierzchnię.
    surf2 = ax2.plot_surface(A, B, D, cmap =cm.coolwarm,
    linewidth = 0 , antialiased = False)
    ax2.set_zlim(-1.01 , 1.01)
    ax2.zaxis.set_major_locator(LinearLocator(10))
    ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf1, shrink=0.5, aspect=5)
    fig.colorbar(surf2, shrink=0.5, aspect=5)
    plt.show()


zad_1()
zad_2()
zad_3()
zad_4()
zad_5()
