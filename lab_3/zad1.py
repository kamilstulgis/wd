# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A={1/x: x∈<1,10>}
# B={1, 2, 4, 8,…, }
# C={x: x∈ B i x jest liczbą podzielną przez 4}
# a
lista = [1/x for x in range(1,10)]
print(lista)
# b
potega = [2 ** x for x in range(11)]
print(potega)
# c
podzielne= [x for x in potega if x % 4 == 0]
print(podzielne)