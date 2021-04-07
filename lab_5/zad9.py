# Przepisz jeden z napisanych przez siebie iteratorów na generator.

class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def reverse(self):
        for index in range(len(self.data)-1, -1, -1):
            yield self.data[index]

gen = Wspak('slowo').reverse()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print('--------------------------')