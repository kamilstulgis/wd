# Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

def iloczyn_ciagu (* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1.0
    for i in liczby:
        iloczyn *= i
    return iloczyn
print(iloczyn_ciagu())
print(iloczyn_ciagu(2, 1, 4))
print(iloczyn_ciagu(-1, -2, -3))

# def iloczyn_ciagu (a1 = 1, r = 1, ile = 10):
#     i = 0
#     if ile == 0:
#         return 0.0
#     elif a1 > 0:
#         iloczyn = 1.0
#     else:
#         iloczyn = -1.0
#     while i < ile:
#         iloczyn *= a1
#         print(a1)
#         a1 += r
#         i += 1
#     return iloczyn
# print(iloczyn_ciagu())
# print(iloczyn_ciagu(2, 1, 4))
# print(iloczyn_ciagu(-2, -1, 4))
