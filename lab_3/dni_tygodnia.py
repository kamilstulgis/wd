# Stwórz moduł o nazwie dni_tygodnia.py i umieść w nim co najmniej dwie funkcje zwracające polskie nazwy dni tygodnia w zależności od przekazanego parametru. Propozycje: funkcja zwracająca dzień tygodnia dla dowolnej daty przekazanej jako argument, dzień tygodnia na podstawie numeru dnia tygodnia, funkcja zwracająca skrócone nazwy dni tygodnia, funkcja zwracająca słownik par gdzie klucz to dzień miesiąca a wartość to polska nazwa dnia tygodnia dla danego miesiąca przekazanego jako argument funkcji (rok, miesiąc zapewne).

import calendar
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')

def dictionary_date(year, month):
    cal = calendar.Calendar()
    months = calendar.monthrange(year, month)
    week = int(months[0])
    days = int(months[1]+1)
    print()
    for day in range(1,days):
        list = {day:calendar.day_name[week % 7]}
        week+=1
        print(list)
# dictionary_date(2021, 3)

def name_of_day(year, month, day):
    if day > 0 and day <= 31:
        data = {day: calendar.weekday(year, month, day)}
        nr_day = data[day]
        days = {day: calendar.day_name[nr_day]}
        return days
    else:
        return 'Podaj prawdziwa datę'
# print(name_of_day(1993,3,22))

def day_name(year, month, day):
    if day > 0 and day <= 31:
        dzien = calendar.day_name[day % 7-1]
        return dzien
    else:
        return 'Podaj prawdziwa datę'
# print(day_name(1993,3,26))
# # Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

def full_date(full_data):
    data = full_data.split(' ')
    day = int(data[0])
    return calendar.day_name[day % 7-1]
# print(full_date('26 03 2021'))

def day(nr):
    return calendar.day_name[nr % 7-1]
# print(day(4))
    # dni = {1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek',  6: 'Sobota', 7: 'Niedziela'}
    # if nr >= 1 and nr <= 7:
    # else:
        # return 'Tydzień ma tylko siedem dni'

def short_name(nr):
    dni = {1: 'PN', 2: 'WT', 3: 'ŚR', 4: 'CZW', 5: 'PT',  6: 'SB', 7: 'NDZ'}
    if nr >= 1 and nr <= 7:
        return dni[nr]
    else:
        return 'Tydzień ma tylko siedem dni'
# print(short_name(4))