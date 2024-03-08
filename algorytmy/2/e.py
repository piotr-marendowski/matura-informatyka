# rekurencja super ekstraklasa
# 3 znaczniki
# nieskonczona petla
# dopoki lewy (najmniejsza) nie przekroczy prawego znacznika (najwyzsza) i
# kiedy znacznik lewy jest mniejszy lub rowny od znacznika poczatkowego
# idz dalej
# to samo tylko przemieszczamy najwyzsza w lewo
# potem lewy (najmniejsza) wskazuje na element, ktory jest wiekszy, a prawy (najwyzsza)
# wskazuje na element, ktory jest nizszy, czyli odwrotnie niz powinno byc
# i sie zamieniaja miejscami jesli najmniejsza jest mniejsza niz najwyzsza
# jesli sie juz zamienily miejscami to przerwij petle
# wymien znacznik z najmniejsza, bo po lewej od najmniejszej sa mniejsze od niego
# zwroc najmniejsza
def podziel(liczby, start, koniec):
    znacznik = liczby[koniec]
    najmniejsza = start
    najwyzsza = koniec - 1

    while True:
        while najmniejsza <= najwyzsza and liczby[najmniejsza] <= znacznik:
            najmniejsza += 1

        while najmniejsza <= najwyzsza and liczby[najwyzsza] >= znacznik:
            najwyzsza -= 1

        if najmniejsza <= najwyzsza:
            liczby[najmniejsza], liczby[najwyzsza] = liczby[najwyzsza], liczby[najmniejsza]
        else:
            break

    liczby[koniec], liczby[najmniejsza] = liczby[najmniejsza], liczby[koniec]

    return najmniejsza


# wykonuj tylko kiedy lista jest niezerowa i wieloelementowa
# potem tworzymy znacznik, ktorego miejsce jest takie same jak poprzedniego znacznika
# i lecimy do lewej strony
# i potem w prawa strone
def quicksort(liczby, start, koniec):
    if start < koniec:
        znacznik = podziel(liczby, start, koniec)
        quicksort(liczby, start, znacznik - 1)
        quicksort(liczby, znacznik + 1, koniec)
        print(liczby)


liczby = [8, 2, 1, 9, 5]
print(liczby)

quicksort(liczby, 0, len(liczby) - 1)
