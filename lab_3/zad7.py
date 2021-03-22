# Zdefiniuj funkcję, która oblicza długość przeciwprostokątnej, wykorzystując twierdzenie pitagorasa. Proszę podać wartości domyślne dla funkcji
import math

def pitagoras(a = 0, b = 0):
    return pow(((pow(a,2)) + pow(b,2)),0.5)
    # return math.sqrt(((pow(a,2)) + pow(b,2)))

print(pitagoras(4,3))
print(pitagoras())