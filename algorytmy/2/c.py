# idz od drugiego elementu do konca (pierwszy jest juz "posortowany")
# przypisz min do aktualnego elementu
# idz w poprzednie elementy i zamieniaj je jesli sa wieksze od
# aktualnej liczby
# i potem sprawdzaj nastepna liczbe w liscie
def wstawianie1(liczba):
    for i in range(1, len(liczby)):
        min = liczby[i]

        j = i - 1
        while j >= 0 and min < liczby[j]:
            liczby[j + 1] = liczby[j]
            j -= 1

        liczby[j + 1] = min

    print(f"   {liczby}\n")


liczby = [4, 8, 12, 3, 7, 7, 6]
print(f"1: {liczby}")
wstawianie1(liczby)

# odwrotna wersja (dluzsza ale prostsza)
# idziemy przez cala liste od poczatku
# aktualny element jest najmniejszy
# idz od aktualnego do konca
# porownuj ta aktualna z nastepna
# i zamien je jesli ta aktualna jest mniejsza
# i tak w kolko
# i na koncu odwroc liste
def wstawianie2(liczba):
    for i in range(0, len(liczby)):
        min = i

        for j in range(i + 1, len(liczby)):
            if liczby[min] < liczby[j]:
                liczby[j], liczby[min] = liczby[min], liczby[j]

    print(f"   {liczby[::-1]}")


liczby = [4, 8, 12, 3, 7, 7, 6]
print(f"2: {liczby}")
wstawianie2(liczby)
