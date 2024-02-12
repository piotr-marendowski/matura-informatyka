# Piotr Marendowski, GNU GPL v.3
# Konwersja systemow liczbowych

# Uzywajac wbudowanych funkji
# a) DEC -> BIN,
def dec_to_bin(dec_list):
    bin_list = []

    # Funkcja bin(int)[2:]
    # [2:] usuwa 2 pierwsze miejsca (0b)
    for num in dec_list:
        bin_list.append(bin(num)[2:])

    print("DEC -> BIN:")
    print("  ".join(bin_list))

    return bin_list


# b) BIN -> DEC,
def bin_to_dec(bin_list):
    dec_list = []

    for num in bin_list:
        dec_list.append(int(num, 2))

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("BIN -> DEC:")
    print("  ".join(dec_list))


# c) DEC -> HEX,
def dec_to_hex(dec_list):
    hex_list = []

    for num in dec_list:
        hex_list.append(hex(num)[2:])

    # Zamiana z int na string, zeby wyswietlic
    dec_list = [str(num) for num in dec_list]

    print("DEC -> HEX:")
    print("  ".join(hex_list))

    return hex_list


# d) HEX -> DEC,
def hex_to_dec(hex_list):
    dec_list = []

    for num in hex_list:
        dec_list.append(int(num, 16))

    print("HEX -> DEC:")
    # Wyswietl inty bez konwersji na stringi
    print(*dec_list, sep="  ")


# e) DEC -> OCT,
def dec_to_oct(dec_list):
    oct_list = []

    for num in dec_list:
        oct_list.append(oct(num)[2:])
        # Mozna tez konwertowac w trakcie wtf (linked listy to sa pewnie)
        str(num)

    print("DEC -> OCT:")
    print("  ".join(oct_list))

    return oct_list


# f) OCT -> DEC,
def oct_to_dec(oct_list):
    print("OCT -> DEC:")

    # Wyswietl w jednej linii z dwiema przerwami
    for num in oct_list:
        print(int(num, 8), end="  ")

    # Przez ten `end=` musi to byc zeby nastepny print by w nowej linii
    print("")


# g) HEX -> BIN,
def hex_to_bin(hex_list):
    print("HEX -> BIN:")

    for num in hex_list:
        print(bin(int(num, 16))[2:], end="  ")

    print("")


# h) BIN -> HEX,
def bin_to_hex(bin_list):
    print("BIN -> HEX:")

    for num in bin_list:
        print(hex(int(num, 2))[2:], end="  ")

    print("")


# i) OCT -> BIN,
def oct_to_bin(oct_list):
    print("OCT -> BIN:")

    for num in oct_list:
        print(bin(int(num, 8))[2:], end="  ")

    print("")


# j) BIN -> OCT
def bin_to_oct(bin_list):
    print("BIN -> OCT:")

    for num in bin_list:
        print(oct(int(num, 2))[2:], end="  ")

    print("")


# k) DEC -> p (dowolny)
def dec_to_p(dec_list):
    print("DEC -> p (dowolny):")


def main():
    dec_list = [0, 1, 2, 4, 5, 6, 10, 11, 18, 19, 25, 37, 44]
    # przekonwertuj liste intow na liste stringow i wyswietl bez '[' i '''
    dec_str_list = [str(num) for num in dec_list]
    print("Oryginalna lista:")
    print("  ".join(dec_str_list), "\n")

    # Uzywajac wbudowanych funkji
    print("Uzywajac wbudowanych funkji:")
    # a) DEC -> BIN,
    bin_list = dec_to_bin(dec_list)
    # b) BIN -> DEC,
    bin_to_dec(bin_list)
    # c) DEC -> HEX,
    hex_list = dec_to_hex(dec_list)
    # d) HEX -> DEC,
    hex_to_dec(hex_list)
    # e) DEC -> OCT,
    oct_list = dec_to_oct(dec_list)
    # f) OCT -> DEC,
    oct_to_dec(oct_list)
    # g) HEX -> BIN,
    hex_to_bin(hex_list)
    # h) BIN -> HEX,
    bin_to_hex(bin_list)
    # i) OCT -> BIN,
    oct_to_bin(oct_list)
    # j) BIN -> OCT
    bin_to_oct(bin_list)
    # k) DEC -> p (dowolny)
    dec_to_p(dec_list)


    # Uzywajac wlasnych funkji konwersji


if __name__ == "__main__":
    main()
