# Za pomocą wyrażenia generującego stwórz generator zwracający polskie nazwy miesięcy.

def rok_kalendarzowy():
    miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

    for i in range(0, 12):
        yield miesiace[i]

miesiace = rok_kalendarzowy()
for miesiac in range(0, 12):
    print(next(miesiace))
