# Przetestuj powyższy iterator na kilku różnych kolekcjach.

class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

kolekcja = Wspak(['t','e','k','s','t','o','d','t','y','l','u'])

print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print('--------------------------')

tekst = Wspak(['k','a','j','a','k','i'])

print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print('---------------')