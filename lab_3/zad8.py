def ciag(a1= 1, r=2, ile=10):
    i = a1
    if ile == 0:
        return 0.0
    else:
        suma = 0.0
    while i <= ile:
        suma += a1
        a1 += r
        i += 1
    return suma

print(ciag())
# print(ciag(2,3,4))