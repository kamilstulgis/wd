import pandas as pd
import numpy as np
import xlrd
import openpyxl

print('Zadanie1')
df = pd.read_excel('imiona.xlsx')
print('##########')
"""
Zadanie 2
Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

1.tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
2.tylko rekordy gdzie nadane imię jest takie jak Twoje
3.sumę wszystkich urodzonych dzieci w całym danym okresie,
4.sumę dzieci urodzonych w latach 2000-2005
5.sumę urodzonych chłopców i dziewczynek,
6.najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
7.najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
"""

print("Zadanie 2.1")
df2_1= df.copy()
df2_1[df2_1['Liczba'] > 1000].to_excel('2_1.xlsx',  sheet_name='1000')
print('##########')

print("Zadanie 2.2")
df2_2 = df.copy()
# print(df2_2.loc[df.Imie=='KAMIL'])
df2_2.loc[df.Imie=='KAMIL'].to_excel('2_2.xlsx',  sheet_name='Kamil')
print('##########')

print("Zadanie 2.3")
df2_3 = df.copy()
print(df2_3.agg({'Liczba':['sum']}))
print('##########')

print("Zadanie 2.4")
df2_4 = df.copy()
print(df2_4[df2_4['Rok'] <= 2005].agg({'Liczba':['sum']}))
print('##########')

print("Zadanie 2.5")
df2_5 = df.copy()
print('Chłopcy')
print(df2_5[df2_5['Plec'] == 'M'].agg({'Liczba':['sum']}))
print('Dziweczynki')
print(df2_5[df2_5['Plec'] == 'K'].agg({'Liczba':['sum']}))
print('#####################')
print(df2_5.groupby(['Plec']).agg({'Liczba':['sum']}))
print('#####################')

print("Zadanie 2.6")
df2_6 = df.copy()
print('#####################')
dd=df2_6.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
print(dd)
print('#####################')

print("Zadanie 2.7")
df2_7 = df.copy()

chlopiec = df2_7[df2_7['Plec'] == 'M'].Liczba.max()
dziewczyna = df2_7[df2_7['Plec'] == 'K'].Liczba.max()
print(df2_7[df2_7['Liczba'] == chlopiec])
print(df2_7[df2_7['Liczba'] == dziewczyna])
# print(df2_7.groupby(['Plec']).Liczba.max())
# print('--------------------------------------')

print('##########')

"""
Zadanie 3
Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:

1. istę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
2. 5 najwyższych wartości zamówień
3. ilość zamówień złożonych przez każdego sprzedawcę
4. sumę zamówień dla każdego kraju
5. sumę zamówień dla roku 2005, dla sprzedawców z Polski
6. średnią kwotę zamówienia w 2004 roku,
7. zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
"""

print('Zadanie 3_1')
df3 = pd.read_csv('zamowienia.csv', delimiter=';')
print(df3.Sprzedawca.unique())

print('Zadanie 3_2')
print(df3.sort_values(by='Utarg', ascending=False).iloc[:5])

print('Zadanie 3_3')
print(df3.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))

print('Zadanie 3_4')
print(df3.groupby(['Kraj']).agg({'Utarg': ['sum']}))

print('Zadanie 3_5')

print('----------------------------------')
print(df3[( (df3['dataZamowienia'] >= '2005-01-01') & (df3['dataZamowienia'] <= '2005-12-31') & (df3['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))
print('----------------------------------')

print(df3['dataZamowienia'])
print('Zadanie 3_6')
print('Zadanie 3_7')