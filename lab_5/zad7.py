# Przetestuj powyższy iterator na kilku różnych kolekcjach.

class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.start = -2
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.start:
            raise StopIteration
        self.start = self.start + 2
        return self.data[self.start]

kolekcja = Wspak(['t','e','k','s','t','o','d','t','y','l','u'])

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
print('---------------')