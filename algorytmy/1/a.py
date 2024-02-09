# Piotr Marendowski, GNU GPL v.3

# g) HEX -> BIN,
# h) BIN -> HEX,
# i) OCT -> BIN,
# j) BIN -> OCT
# k) DEC -> p (dowolny)


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
        # Mozna tez konwertowac w trakcie wtf (linked listy to moga byc po prostu)
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


dec_list = [0, 1, 2, 4, 5, 6, 10, 11, 18, 19, 25, 37, 44]
# przekonwertuj liste intow na liste stringow i wyswietl bez '[' i '''
dec_str_list = [str(num) for num in dec_list]
print("Oryginalna lista:")
print("  ".join(dec_str_list), "\n")

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
