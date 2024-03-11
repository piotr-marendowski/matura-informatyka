# funkcja f(x) bo tak
def f(x):
    return -4 * x + 2


# a i b -> granice przedzialu
# jesli fukcje nie maja roznych znakow to nie ma pierwiastkow
# dopoki dwa konce sa w miare duze, to oblicza srodek
# jesli f(srodka) jest 0 to jest pierwiastek
# jesli jesli f(srodka) * f(a) jest mniejsza od 0, to
# znaczy ze pierwiastek jest w przedziale (a, srodek), wiec
# zmienia b na srodek
# odwrotnie jest przedzial (srodek, b)
# i tak idzie w coraz mniejsze liczby az bedzie dosc dokladnie
# w miejscu zerowym
def miejca_zerowe(a, b, precyzja=0.00001):
    if f(a) * f(b) >= 0:
        return None

    srodek = a
    while b - a >= precyzja:
        srodek = (a + b) / 2

        if f(srodek) == 0.0:
            break

        if f(srodek) * f(a) < 0:
            b = srodek
        else:
            a = srodek

    return srodek


print(f"Miejsce zerowe od -10 do 10: {miejca_zerowe(-10, 10, 0.00001)}")
