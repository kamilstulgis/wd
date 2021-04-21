import numpy as np

"""Zadanie 1
Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia."""

# z = np.array([1,2,3])
# y = np.array([2,2,2])
# c = z * y
# print(c)

"""Zadanie 2
Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu."""

# c = np.arange(9).reshape((3,3))
# d = np.arange(16).reshape((4,4))

# print(c)
# print(c.min(axis=1))
# print(c.min(axis=0))
# print('----------')
# print(d)
# print(d.min(axis=1))
# print(d.min(axis=0))

"""Zadanie 3
Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy."""

# print(z.dot(y))
# print(np.dot(z,y))

"""Zadanie 4
Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia."""

# f = np.array([1,2,3])
# g = np.array([-3, 0.5,3.14])
# h = f * g
# print(h)

"""Zadanie 5
Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”."""

# i = np.arange(6).reshape((2,3))
# a = np.sin(i)
# print(a)

"""Zadanie 6
Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”."""

# print('----------')
# j = np.arange(6).reshape(2,3)
# b = np.cos(j)
# print(b)

"""Zadanie 7
Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b."""

# print('----------')
# k = a + b

# print(k)

"""Zadanie 8
Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów."""

# l = np.arange(9).reshape((3,3))

# for el in l:
#     print(el)
#     print('---')

"""Zadanie 9
Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy."""

# m = np.arange(9).reshape((3,3))

# for el in m.flat:
#     print(el)

"""Zadanie 10
Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?"""

# n = np.arange(81).reshape((9,9))
# o = n.T
# p = n.reshape((3,27))
# r = n.reshape((27,3))
# s = n.reshape((1,81))
# t = n.reshape((81,1))

# print('------')
# print(n)
# print(n.shape)

# print('------')
# print(o)
# print(o.shape)

# print('------')
# print(p)
# print(p.shape)

# print('------')
# print(r)
# print(r.shape)

# print('------')
# print(s)
# print(s.shape)

# print('------')
# print(t)
# print(t.shape)

"""Zadanie 11
Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?"""

w = np.arange(12)
print(w)

print('-----------')
w1= w.reshape((3,4))
w11 = w1.ravel()
print(w1)
print(w11)

print('-----------')
w2= w1.reshape((4,3))
w22 = w2.ravel()
print(w2)
print(w22)

print('-----------')
w3= w.reshape((2,6))
w33 = w3.ravel()
print(w3)
print(w33)