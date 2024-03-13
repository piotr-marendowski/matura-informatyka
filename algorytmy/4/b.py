# zamieniamy na male i usuwamy spacje
# wypisujemy roznice posortowanych zdan
def anagram1(zdanie1, zdanie2):
    zdanie1 = zdanie1.lower().replace(" ", "")
    zdanie2 = zdanie2.lower().replace(" ", "")

    print(sorted(zdanie1) == sorted(zdanie2))


# zamieniamy na male i usuwamy spacje
# tworzymy hash table czy jak to tam sie nazywa
# jesli nie sa tak samo dlugie to nie sa anagramami
# najpierw lecimy przez wszystkie elementy pierwszego zdania i
# zliczamy je
# potem lecimy przez drugie zdanie i odejmujemy napotkane w obu zdaniach litery
# lecimy przez caly hash table i jesli znajdziemy jakas litere,
# ktora zostala, to znaczy ze to nie byly anagramy
def anagram2(zdanie1, zdanie2):
    zdanie1 = zdanie1.lower().replace(" ", "")
    zdanie2 = zdanie2.lower().replace(" ", "")

    hash_table = dict()

    if len(zdanie1) != len(zdanie2):
        return False
    else:
        for i in zdanie1:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in zdanie2:
            if i in hash_table:
                hash_table[i] -= 1
            else:
                hash_table[i] = 1

        for i in hash_table:
            if hash_table[i] != 0:
                return False

    return True


zdanie1 = "fairy tales"
zdanie2 = "rail safety"
anagram1(zdanie1, zdanie2)
print(anagram2(zdanie1, zdanie2))
