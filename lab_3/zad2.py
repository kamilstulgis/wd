# Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj listę, która będzie zawierała tylko elementy znajdujące się na przekątnej.

import random # biblioteka z funkcjami do losowania

macierz = [[random.randint(1,10) for i in range(4)]  for j in range(4)]

przekatna = [macierz[x][x] for x in range(4)]
print(macierz)
print(przekatna)


# y=[]
# for i in range(4):
#     x=[]
#     for j in range (4):
#         x.append(random.randint(1,50))
#     print(x)
#     y.append(x[i])
# print(y)

# ciekawa petla do wyswietlania wierszy
# for wiersz in macierz:
    # print(wiersz)

# print([2, 4, 5, 6])
# print([1, 3, 1, 7])
# print([4, 2, 4, 8])
# print([9, 5, 5, 2])
# # wynik
# print([2,3,4,2])