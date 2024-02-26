# Szuka czynnikow pierwszych, czyli liczb pierwszych (tych co dziela sie tylko
# przez 1 i siebie), ktore mnozac siebie wszystkie otrzymaja ta wlasnie liczbe poczatkowa
# oczywiscie szukamy liczby wiekszej od 1
# dopoki liczby juz sie nie da podzielic:
# idziemy dopoki znajdujemy dzielnik liczby (np. 10 / 2 = dzielnik, bo bez reszty)
# i go dodajemy do listy czynnikow
# i dzielimy przez niego liczbe (jesli sie da podzielic, to znaczy ze jest czynnikiem (aka liczba pierwsza), bo idziemy przeciez od najnizszej mozliwej liczby)
# potem jak juz nie mozemy podzielic naszej liczby, to probujemy z nastepna i tak w kolko
def czynniki(liczba):
    czynniki = []
    dzielnik = 2

    if liczba > 1:
        while liczba != 1:
            while liczba % dzielnik == 0:
                czynniki.append(dzielnik)
                liczba //= dzielnik
            dzielnik += 1

    print(czynniki)

czynniki(30)
