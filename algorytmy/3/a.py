# w skrocie:
# jesli 0 potega to 1 wiadomo
# jesli n jest nieparzysta, to mnozy mniejsza rekurencje przez a (normalne mnozenie)
# jesli jest parzysta, to oblicza potege a (potega)
def szybka_potega(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * szybka_potega(a, n - 1)
    else:
        a = szybka_potega(a, n // 2)
        return a * a


print(szybka_potega(2, 10))
