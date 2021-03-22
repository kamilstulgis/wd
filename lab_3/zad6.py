# Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia. Funkcja ma przyjmować argumenty domyślne: Równanie okręgu dane jest wzorem:
# (x-a)2+(y-b)2=r2 gdzie (a,b) to środek okręgu a r to promień okręgu.
import math

def promien(a = 0, b = 0, y = 0, x = 0):
    return pow( pow((x-a),2) + pow((y-b),2),0.5)
    # return math.sqrt( pow((x-a),2) + pow((y-b),2))
print(promien(1,2,3,4))
print(promien())