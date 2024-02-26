# NWD z odejmowaniem iteracyjnie
# dopoki nie sa takie same (wtedy znajdziemy nwd)
# sprawdzamy ktora liczba jest wieksza
# i odejmujemy od niej mniejsza
# i tak w kolko az liczby beda takie same, co oznacza ze
# to jest ich najwiekszy wspolny dzielnik
def nwd_od_it(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print("1. NWD(60, 48):", nwd_od_it(60, 48))

# NWD z odejmowaniem rekurencyjnie
# jesli a jest rozne od b:
# i sprawdzamy czy a jest wieksze od b
# i pomniejszamy mniejsza wartosc o ta wieksza
# jak a bedzie rowne b to mamy dla nich nwd
def nwd_od_re(a, b):
    if a != b:
        if a > b:
            return nwd_dz_re(a - b, b)
        else:
            return nwd_dz_re(b, a - b)


print("2. NWD(60, 48):", nwd_od_re(60, 48))


# NWD z dzieleniem iteracyjnie
# dopoki b nie jest 0:
# przypisz b do a, i reszte z dzielenia a i b do b
# i tak w kolko az b nie jest 0, wtedy a jest nwd
def nwd_dz_it(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print("3. NWD(60, 48):", nwd_dz_it(60, 48))

# NWD z dzieleniem rekurencyjnie
# jesli b jest 0 to wtedy mamy nwd
# lub idz dalej i wywoluj rekurencyjnie ta sama funkcje,
# w skrocie dzielac w dol a i b przez siebie, az dojdziemy do 0 w b
# i wtedy b jest 0 czyli a to nasze nwd
def nwd_dz_re(a, b):
    if b == 0:
        return a
    else:
        return nwd_dz_re(b, a % b)


print("4. NWD(60, 48):", nwd_dz_re(60, 48))
