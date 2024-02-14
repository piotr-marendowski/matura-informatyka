# Piotr Marendowski, GNU GPL v.3
# Konwersja systemow liczbowych

#################################################
# Uzywajac wbudowanych funkji konwersji         #
#################################################

# DEC -> BIN,
def dec_to_bin(dec_list):
    bin_list = []

    # Funkcja bin(int)[2:]
    # [2:] usuwa 2 pierwsze miejsca (0b)
    for num in dec_list:
        bin_list.append(bin(num)[2:])

    print("DEC -> BIN:")
    print("  ".join(bin_list))

    return bin_list


# BIN -> DEC,
def bin_to_dec(bin_list):
    dec_list = []

    for num in bin_list:
        dec_list.append(int(num, 2))

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("BIN -> DEC:")
    print("  ".join(dec_list))


# DEC -> HEX,
def dec_to_hex(dec_list):
    hex_list = []

    for num in dec_list:
        hex_list.append(hex(num)[2:])

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("DEC -> HEX:")
    print("  ".join(hex_list))

    return hex_list


# HEX -> DEC,
def hex_to_dec(hex_list):
    dec_list = []

    for num in hex_list:
        dec_list.append(int(num, 16))

    print("HEX -> DEC:")
    # Wyswietl inty bez konwersji na stringi
    print(*dec_list, sep="  ")


# DEC -> OCT,
def dec_to_oct(dec_list):
    oct_list = []

    for num in dec_list:
        oct_list.append(oct(num)[2:])
        # Mozna tez konwertowac w trakcie wtf (linked listy to sa pewnie)
        str(num)

    print("DEC -> OCT:")
    print("  ".join(oct_list))

    return oct_list


# OCT -> DEC,
def oct_to_dec(oct_list):
    print("OCT -> DEC:")

    # Wyswietl w jednej linii z dwiema przerwami
    for num in oct_list:
        print(int(num, 8), end="  ")

    # Przez ten `end=` musi to byc zeby nastepny print by w nowej linii
    print("")


# HEX -> BIN,
def hex_to_bin(hex_list):
    print("HEX -> BIN:")

    for num in hex_list:
        print(bin(int(num, 16))[2:], end="  ")

    print("")


# BIN -> HEX,
def bin_to_hex(bin_list):
    print("BIN -> HEX:")

    for num in bin_list:
        print(hex(int(num, 2))[2:], end="  ")

    print("")


# OCT -> BIN,
def oct_to_bin(oct_list):
    print("OCT -> BIN:")

    for num in oct_list:
        print(bin(int(num, 8))[2:], end="  ")

    print("")


# BIN -> OCT
def bin_to_oct(bin_list):
    print("BIN -> OCT:")

    for num in bin_list:
        print(oct(int(num, 2))[2:], end="  ")

    print("")


#################################################
# Uzywajac wlasnych funkji konwersji            #
#################################################

# DEC -> BIN,
def dec_to_bin_konwersja(liczba):
    liczba_bin = ""

    # Dopoki liczba nie jest w najprostrzej postaci,
    # dopisz liczbe zmodulowana przez 2,
    # dziel liczbe przez 2,
    # i tak w kolko
    #
    # Podzielna = 0, czyli nie dodaje sie
    # Niepodzielna = 1, czyli dodaje sie tworzac liczbe,
    # np. 10100 = 20 (16 + 4)
    while liczba > 0:
        # print(f"liczba: {liczba}")
        liczba_bin = str(liczba % 2) + liczba_bin
        # // znaczy podziel i zaookragl (funkcja floor)
        liczba = liczba // 2
        # print(f"liczba_bin: {liczba_bin}")

    return liczba_bin


def dec_to_bin2(dec_list):
    bin_list = []

    print("DEC -> BIN:")

    for num in dec_list:
        bin_num = dec_to_bin_konwersja(num)
        bin_list.append(bin_num)
        print(bin_num, end="  ")

    return bin_list


# BIN -> DEC,
def bin_to_dec2(bin_list):
    dec_list = []

    for num in bin_list:
        dec_list.append(int(num, 2))

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("BIN -> DEC:")
    print("  ".join(dec_list))


# DEC -> HEX,
def dec_to_hex2(dec_list):
    hex_list = []

    for num in dec_list:
        hex_list.append(hex(num)[2:])

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("DEC -> HEX:")
    print("  ".join(hex_list))

    return hex_list


# HEX -> DEC,
def hex_to_dec2(hex_list):
    dec_list = []

    for num in hex_list:
        dec_list.append(int(num, 16))

    print("HEX -> DEC:")
    # Wyswietl inty bez konwersji na stringi
    print(*dec_list, sep="  ")


# DEC -> OCT,
def dec_to_oct2(dec_list):
    oct_list = []

    for num in dec_list:
        oct_list.append(oct(num)[2:])
        # Mozna tez konwertowac w trakcie wtf (linked listy to sa pewnie)
        str(num)

    print("DEC -> OCT:")
    print("  ".join(oct_list))

    return oct_list


# OCT -> DEC,
def oct_to_dec2(oct_list):
    print("OCT -> DEC:")

    # Wyswietl w jednej linii z dwiema przerwami
    for num in oct_list:
        print(int(num, 8), end="  ")

    # Przez ten `end=` musi to byc zeby nastepny print by w nowej linii
    print("")


# HEX -> BIN,
def hex_to_bin2(hex_list):
    print("HEX -> BIN:")

    for num in hex_list:
        print(bin(int(num, 16))[2:], end="  ")

    print("")


# BIN -> HEX,
def bin_to_hex2(bin_list):
    print("BIN -> HEX:")

    for num in bin_list:
        print(hex(int(num, 2))[2:], end="  ")

    print("")


# OCT -> BIN,
def oct_to_bin2(oct_list):
    print("OCT -> BIN:")

    for num in oct_list:
        print(bin(int(num, 8))[2:], end="  ")

    print("")


# BIN -> OCT
def bin_to_oct2(bin_list):
    print("BIN -> OCT:")

    for num in bin_list:
        print(oct(int(num, 2))[2:], end="  ")

    print("")


# DEC -> p (dowolny)
def dec_to_p(dec_list):
    print("DEC -> p (dowolny):")
    # p = input("Podaj system liczbowy (np. 10): ")

    print("")


def main():
    dec_list = [0, 1, 2, 4, 5, 6, 10, 11, 18, 19, 25, 37, 44]
    # przekonwertuj liste intow na liste stringow i wyswietl bez '[' i '''
    dec_str_list = [str(num) for num in dec_list]
    print("Oryginalna lista:")
    print("  ".join(dec_str_list), "\n")

    # Uzywajac wbudowanych funkji
    print("Uzywajac wbudowanych funkji:")
    dec_to_bin_konwersja(10)
    # DEC -> BIN,
    bin_list = dec_to_bin(dec_list)
    # BIN -> DEC,
    bin_to_dec(bin_list)
    # DEC -> HEX,
    hex_list = dec_to_hex(dec_list)
    # HEX -> DEC,
    hex_to_dec(hex_list)
    # DEC -> OCT,
    oct_list = dec_to_oct(dec_list)
    # OCT -> DEC,
    oct_to_dec(oct_list)
    # HEX -> BIN,
    hex_to_bin(hex_list)
    # BIN -> HEX,
    bin_to_hex(bin_list)
    # OCT -> BIN,
    oct_to_bin(oct_list)
    # BIN -> OCT
    bin_to_oct(bin_list)

    # Uzywajac wlasnych funkji konwersji
    dec_str_list = [str(num) for num in dec_list]
    print("\n\nOryginalna lista:")
    print("  ".join(dec_str_list), "\n")
    print("Uzywajac wlasnych funkji konwersji:")
    # DEC -> BIN,
    bin_list = dec_to_bin2(dec_list)
    # # BIN -> DEC,
    # bin_to_dec2(bin_list)
    # # DEC -> HEX,
    # hex_list = dec_to_hex2(dec_list)
    # # HEX -> DEC,
    # hex_to_dec2(hex_list)
    # # DEC -> OCT,
    # oct_list = dec_to_oct2(dec_list)
    # # OCT -> DEC,
    # oct_to_dec2(oct_list)
    # # HEX -> BIN,
    # hex_to_bin2(hex_list)
    # # BIN -> HEX,
    # bin_to_hex2(bin_list)
    # # OCT -> BIN,
    # oct_to_bin2(oct_list)
    # # BIN -> OCT
    # bin_to_oct2(bin_list)
    # # DEC -> p (dowolny)
    # dec_to_p(dec_list)


if __name__ == "__main__":
    main()
