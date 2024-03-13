# zmniejszamy i usuwamy spacje
# ze stringow tworzymy listy
# idziemy przez cala dlugosc zdania
# jesli jest w nim litera ze wzorca, to:
# idziemy przez nastepne elementy zdania i porownujemy z
# elementami wzorca, jesli nie sa rowne, to false
def wyszukaj(zdanie, wzorzec):
    zdanie = zdanie.lower().replace(" ", "")

    zdanie = list(zdanie)
    wzorzec = list(wzorzec)

    i = 0
    while i != len(zdanie) - 1:
        i += 1
        if zdanie[i] == wzorzec[0]:
            for j in range(1, len(wzorzec)):
                i += 1
                if zdanie[i] != wzorzec[j]:
                    return False

    return True


zdanie = "Nie szukaj wzorca!"
wzorzec = "szuka"
print(wyszukaj(zdanie, wzorzec))
