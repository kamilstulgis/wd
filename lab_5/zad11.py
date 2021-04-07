# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego

def fibo(ile_razy):
    f1= 0
    f2= 1
    suma = 0
    for index in range(0,ile_razy):
        yield f1
        suma = f1+f2
        f1 = f2
        f2 = suma

print(tuple(fibo(10)))

