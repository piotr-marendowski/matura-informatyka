# najpierw deklarujemy nominaly (musza byc od najwiekszego)
# iteracyjnie lecimy przez nominaly, dzielimy kwote przez nominal, czyli
# wychodzi ilosc nominalow, bo nie ma reszty
# potem zmniejszamy kwote o ilosc tych nominalow, czyli odejmujemy je od
# lacznej kwoty i zostaje reszta
# np. 250:
# ilosc = 250 / 200 => 2 (bez reszty)
# kwota = 250 % 200 => 50 reszty

def reszta(kwota):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    ilosc = 0

    for i in nominaly:
        ilosc += kwota // i
        kwota %= i

    return ilosc


kwota = 49

print(f"{kwota} zl, ilosc monet/banknotow = {reszta(kwota)}")
