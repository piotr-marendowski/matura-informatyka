# idziemy przez cala liste po kolei, element po elemencie
# zaznaczamy, ze pierwszy rozpatrzany numer elementu to min,
# bo on jest pierwszy (w nastepnych iteracjach wstawiamy tutaj najmniejsza
# wartosc, wiec wiemy, ze mozemy zaczac porownywanie od nastepnego elementu)
# potem idziemy od nastepnego elementu do konca i
# po kolei porownujemy z nim i szukamy najmniejszej
# potem zamieniamy miejscami, aktualny element z najmniejszym
# i tak w kolko
def wybor(liczby):
    for i in range(len(liczby)):
        min = i

        for j in range(i + 1, len(liczby)):
            if liczby[min] > liczby[j]:
                min = j

        liczby[i], liczby[min] = liczby[min], liczby[i]

    print(liczby)


liczby = [4, 8, 12, 3, 7, 7, 6, 5, 0]
print(liczby)
wybor(liczby)
