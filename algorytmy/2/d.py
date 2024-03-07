# rekurencyjna magia w skrocie:
# dzielimy liste na dwie strony i tak w kolko rekurencyjnie
# idziemy i dzielimy na dwie strony az do pojedynczych elementow
# i potem wraca rekurencja i ona laczy z powrotem te elementy, ale
# jednoczesnie porownujac je i sortuje
# i tak idzie az polaczy coraz wieksze grupki elementow posortowanych
# az do polaczenia dwoch najwiekszych grupek w posortowana calosc
def sortowanie(liczby):
    if len(liczby) > 1:
        srodek = len(liczby) // 2
        lewa = liczby[:srodek]
        prawa = liczby[srodek:]

        print(f"lewa:  {lewa}\nprawa: {prawa}")

        sortowanie(lewa)
        sortowanie(prawa)

        i = j = k = 0

        while i < len(lewa) and j < len(prawa):
            if lewa[i] < prawa[j]:
                liczby[k] = lewa[i]
                i += 1
            else:
                liczby[k] = prawa[j]
                j += 1
            k += 1

        while i < len(lewa):
            liczby[k] = lewa[i]
            i += 1
            k += 1

        while j < len(prawa):
            liczby[k] = prawa[j]
            j += 1
            k += 1

        print(f"po:    {liczby}")


liczby = [8, 2, 1, 9, 5]
print(liczby)

sortowanie(liczby)
