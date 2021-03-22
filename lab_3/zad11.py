# import this
# Stwórz moduł o nazwie dni_tygodnia.py i umieść w nim co najmniej dwie funkcje zwracające polskie nazwy dni tygodnia w zależności od przekazanego parametru. Propozycje: funkcja zwracająca dzień tygodnia dla dowolnej daty przekazanej jako argument, dzień tygodnia na podstawie numeru dnia tygodnia, funkcja zwracająca skrócone nazwy dni tygodnia, funkcja zwracająca słownik par gdzie klucz to dzień miesiąca a wartość to polska nazwa dnia tygodnia dla danego miesiąca przekazanego jako argument funkcji (rok, miesiąc zapewne).

import dni_tygodnia

dni_tygodnia.dictionary_date(2021, 3)
print(dni_tygodnia.name_of_day(1993,3,22))
print(dni_tygodnia.day_name(1993,3,26))
print(dni_tygodnia.full_date('26 03 2021'))
print(dni_tygodnia.day(4))
print(dni_tygodnia.short_name(4))