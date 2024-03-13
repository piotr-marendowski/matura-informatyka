# wszystkie znaki na male i usuwamy spacje
# idziemy przez polowe
# i sprawdzamy czy n element od przodu nie jest rowny n elementowi od tylu
# jesli nie jest to znaczy ze to nie jest palindrom
def palindrom1(zdanie):
    zdanie = zdanie.lower().replace(" ", "")

    for i in range(len(zdanie) // 2):
        if zdanie[i] != zdanie[len(zdanie) - 1 - i]:
            return False

    return True


# wszystkie znaki na male i usuwamy spacje
# zwracamy wartosc z pytania czy zdanie rowna sie jemu odworconemu
def palindrom2(zdanie):
    zdanie = zdanie.lower().replace(" ", "")
    return zdanie == zdanie[::-1]


zdanie = input("Podaj zdanie: ")
print("Podane zdanie" + (" " if palindrom1(zdanie) else " nie ") + "jest palindromem")
print("Podane zdanie" + (" " if palindrom2(zdanie) else " nie ") + "jest palindromem")
