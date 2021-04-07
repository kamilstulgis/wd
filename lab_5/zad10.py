# Zaimportuj pakiet itertools i znajdź w jego dokumentacji sposób na wygenerowanie kombinacji 3 elementowych bez powtórzeń na zbiorze 10 elementowym.

import itertools

lista = list(itertools.combinations(range(11), 3))

for element in lista:
    print(element)