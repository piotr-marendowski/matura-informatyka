# s
def sortowanie(liczby, numer):
    output = [0] * len(liczby)
    ilosc = [0] * 10

    for i in range(len(liczby)):
        indeks = liczby[i] // numer
        ilosc[numer % 10] += 1

    for i in range(1, 10):
        ilosc[i] += ilosc[i - 1]

    i = len(liczby) - 1
    while i >= 0:
        indeks = liczby[i] // numer
        output[ilosc[indeks % 10] - 1] = liczby[i]
        ilosc[indeks % 10] -= 1
        i -= 1

    for i in range(len(liczby)):
        liczby[i] = output[i]


def kubelkowe(liczby):
    najwieksza = max(liczby)

    i = 1
    while najwieksza // i > 0:
        sortowanie(liczby, i)
        i *= 10


liczby = [1, 3, 2, 9, 7, 14, 19, 16]
print(liczby)
kubelkowe(liczby)
print(liczby)
