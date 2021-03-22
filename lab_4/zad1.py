# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
liczby = [1,2,3,4,5,6,7,8,9,10,11,12,16,20,24,28,32]

lista = [element for element in liczby if element % 4 == 0]
list = []

plik = open('lab4_zad1.txt', 'a+')

plik.writelines(str(lista))

plik.close()

# for element in liczby:
#     if element % 4 == 0:
#         list.append(element)
# print(list)

# print(lista)

