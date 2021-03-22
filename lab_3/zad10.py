# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to ilość. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać tę wartość.

# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print(f'Lubię {cos}', end='')
#         if len(rzeczy[cos]) > 0:
#             print(f', takie jak {rzeczy[cos]}.')

# to_lubie(slodycze="czekolada", rozrywka=["disco-polo", "moda na sukces"])

def zakupy (** lista):
    suma = 0
    print(f'Twoja lista zakupów to:')
    for wartosc in lista:
        if lista[wartosc] > 0:
            suma += lista[wartosc]
        print(f'{wartosc} : {lista[wartosc]}')
    print(f'Łącznie {suma} produktów')
zakupy(woda = 0, jogurt = 3, chleb = 1, mleko = 2, maslo = 2)