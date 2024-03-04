# bez optymalizacji
# dla ilosc elementow w tablicy lecimy:
# potem znowu przez kazdy element i:
# jesli liczba pierwsza jest wieksza od nastepnej, to
# zamieniamy je miejscami
# i tak lecimy do konca
# i tak lecimy podwojnie przez cala dlugosc tablicy
def bez_optymalizacji(liczby):
    iteracje = 0

    for j in range(len(liczby)):
        for i in range(len(liczby) - 1):
            iteracje += 1
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]

    print("1.", liczby)
    print(f"iteracje: {iteracje}\n")


# pierwsza optymalizacja:
# zamiast idac na slepo przez cala tablice, to
# sprawdzamy czy zamiana sie wykonala kiedykolwiek na calej dlugosci tablicy
# i jesli sie nie wykonala, to znaczy ze tablica jest posortowana
def optymalizacje1(liczby):
    zamiana = True
    iteracje = 0

    while zamiana:
        zamiana = False

        for i in range(len(liczby) - 1):
            iteracje += 1
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]
                zamiana = True

    print("2.", liczby)
    print(f"iteracje: {iteracje}\n")


# druga optymalizacja:
# po prostu odejmujemy ilosc iteracji, poniewaz
# zawsze na koncu kazdej iteracji jest juz posortowany element, ktorego nie przesuniesz
def optymalizacje2(liczby):
    iteracje = 0

    for j in range(len(liczby)):
        for i in range(len(liczby) - 1 - j):
            iteracje += 1
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]

    print("3.", liczby)
    print(f"iteracje: {iteracje}\n")


# trzecia optymalizacja:
# polacz obie optymalizacje
def optymalizacje3(liczby):
    zamiana = True
    iteracje = 0
    koncowa = 0     # ta ostatnia liczba

    while zamiana:
        zamiana = False

        for i in range(len(liczby) - 1 - koncowa):
            iteracje += 1
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]
                zamiana = True

        koncowa += 1

    print("4.", liczby)
    print(f"iteracje: {iteracje}\n")


liczby = [20, 0, 30, 3, 5, 10, 1, 99]
print(liczby, "\n")

bez_optymalizacji(liczby)

liczby = [20, 0, 30, 3, 5, 10, 1, 99]

optymalizacje1(liczby)

liczby = [20, 0, 30, 3, 5, 10, 1, 99]

optymalizacje2(liczby)

liczby = [20, 0, 30, 3, 5, 10, 1, 99]

optymalizacje3(liczby)
