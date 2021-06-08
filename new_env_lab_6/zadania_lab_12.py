from lxml import html
import requests
import pandas as pd
from matplotlib import pyplot as plt

def zad_1():
    url = "https://boardgamegeek.com/"
    data = requests.get(url)
    page = html.fromstring(data.text)

    # pobieramy wszystkie elementy typu <a> gdzie przodkiem jest <H2> oraz elementem nadrzędnym element o
    # klasie "geekcentral_leftcol"
    # xpath = '//*[@class="media-card__title"]//a[@href]'

    xpath='//*[@class="media-card__title"]/a/@href'
    foundElements = page.xpath(xpath)

    for element in foundElements:
        print(element)


def zad_2():

    url = "https://boardgamegeek.com/browse/boardgame"
    data = requests.get(url)

    page = html.fromstring(data.text)
    # tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
    xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
    # można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
    table_div = page.get_element_by_id('collection')

    # w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej
    # należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
    table = table_div.xpath('./*[@class="table-responsive"]/table')[0]
    # print(table)

    # wyświetlamy wszystkie nagłówki tabeli (po przeanalizowaniu dokumentu okazało się, że nie użyto znacznika <thead> do oddzielenia nagłówka tabeli, szukamy więc tylko znaczników <th>)
    labels = [label.strip() for label in table.xpath('.//th/text()')]
    # print(labels)

    # kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
    headers = [label for label in table.xpath('.//th')]
    labels = []
    for header in headers:
        anchor = header.xpath('./a/text()')
        if len(anchor) > 0:
            # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
            labels.append(anchor[0].strip())
        else:
            # trzeba pozbyć się znaków niedrukowalnych
            labels.append(header.text.strip())
    # print(labels)

    """
    Zadanie 2
    Korzystając z kodu z przykładu 4 dodaj kod, który pobierze wszystkie dane z tabeli, z której pobrane zostały nagłówki. Dane następnie zapisz do pandas DataFrame ale wyeliminuj kolumnę, w której jest obraz przedstawiający daną grę oraz kolumnę 'Shop'. Można to zrobić przed wstawieniem danych do frame'a.
    """

    data={}
    for x in labels:
        if x =='' or x=='Shop':continue
        data[x]=[]

    for x in table.xpath('.//*[@id="row_"]'):
        for y in range(len(labels)):
            if labels[y] == '' or labels[y] == 'Shop':continue
            if labels[y] == 'Board Game Rank':
                data[labels[y]].append(int(x.xpath('./td['+str(y+1)+']/a/@name')[0].strip()))
            elif labels[y] == 'Title':
                data[labels[y]].append(x.xpath('./td['+str(y+1)+']/div[2]/a/text()')[0].strip())
            elif labels[y] == 'Num Voters':
                data[labels[y]].append(int(x.xpath('./td['+str(y+1)+']/text()')[0].strip()))
            else:
                data[labels[y]].append(float(x.xpath('./td['+str(y+1)+']/text()')[0].strip()))

    df=pd.DataFrame(data)
    print(df)
    """
    Zadanie 3
    Z DataFrame'a uzyskanego w zadaniu 2 wyświetl 10 rekordów z największymi wartościami w kolumnie 'Num Voters'. Wyświetl również wykres słupkowy dla tych danych.
    """
    grupa = df.sort_values('Num Voters',ascending=False).head(10)
    print(grupa)

    wykres = grupa.plot.bar()
    wykres.set_ylabel('Tyś')
    wykres.legend()
    plt.show()

zad_1()
zad_2()