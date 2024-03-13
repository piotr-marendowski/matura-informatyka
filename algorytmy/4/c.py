# klasyk
def porzadkowanie1(zdanie):
    zdanie = zdanie.lower().replace(" ", "")

    return "".join(sorted(zdanie))


# wiadomo
# tworzy liste zdanie
# sortowanie babelkowe:
# idzie przez wszystkie elementy
# za kazdym razem znowu idzie przez wszystkie
# ale porownujac element aktualny z nastepnym
# i zamienia je jesli nastepny jest mniejszy
# i tak w kolko
def porzadkowanie2(zdanie):
    zdanie = zdanie.lower().replace(" ", "")

    zdanie = list(zdanie)

    for i in range(len(zdanie)):
        for j in range(len(zdanie) - i - 1):
            if zdanie[j] > zdanie[j + 1]:
                zdanie[j + 1], zdanie[j] = zdanie[j], zdanie[j + 1]

    return "".join(zdanie)


zdanie = "Kocham piwo"
print(porzadkowanie1(zdanie))
print(porzadkowanie2(zdanie))
