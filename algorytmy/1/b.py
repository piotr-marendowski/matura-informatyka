# Bierze liczbe n (ktora musi byc wieksza od 1, zeby byc pierwsza)
# i leci n % od 2 do jej samej, szukajac czy ta nasza liczba n jest podzielna
# przez jakas liczbe, jesli nie jest podzielna przez zadna to wtedy jest pierwsza
def parzysta(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(parzysta(1))

# Sito Erastotenesa
# Ciag od 2 do n
# Zainicjuj ciag numerow, ktory ma same wartosci True
# lec przez nie wszystkie
# oczywiscie liczby mniejsze niz 2 nie sa pierwszymi
# dodajemy do liczb pierwszych aktualny numer
# i lecimy od niego do konca (co on kazdy, np. 2 -> 4 -> 6 -> 8... (jego dzielniki))
# i zaznaczamy je jako zlozone, bo tylko on nie dzieli sie przez cos
# i tak w kolko po tych liczbach, ktore jeszcze maja True, czyli sa pierwsze lub nieodkryte jeszcze
def parzysta_ciag(n):
    numery = [True for _ in range(n)]
    pierwsze = []

    for i in range(len(numery)):
        if i <= 1:
            numery[i] = False
        else:
            if numery[i] == True:
                pierwsze.append(i)

                for j in range(i, len(numery), i):
                    numery[j] = False

        # print(f"{i}: {numery}")

    return pierwsze

print(parzysta_ciag(15))
pierwsze = parzysta_ciag(15)

if 7 in pierwsze:
    print("Liczba 7 jest liczba pierwsza")
