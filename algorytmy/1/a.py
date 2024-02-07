# Piotr Marendowski, GNU GPL v.3
#
# c) DEC -> HEX,
# d) HEX -> DEC,
# e) DEC -> OCT,
# f) OCT -> DEC,
# g) HEX -> BIN,
# h) BIN -> HEX,
# i) OCT -> BIN,
# j) BIN -> OCT
# k) DEC -> p (dowolny)


# a) DEC -> BIN,
# Funkcja bin(int)[2:]
# [2:] usuwa 2 pierwsze miejsca (0b)
def dec_to_bin(dec_list):
    bin_list = []

    for num in dec_list:
        bin_list.append(bin(num)[2:])

    print("DEC -> BIN:")
    print(", ".join(bin_list))


# b) BIN -> DEC,
dec_list = [0, 1, 2, 4, 5, 6, 10, 11, 18, 19, 25, 37, 44]
# przekonwertuj liste intow na liste stringow i wyswietl bez '[' i '''
dec_str_list = [str(num) for num in dec_list]
print(", ".join(dec_str_list))

# a) DEC -> BIN,
dec_to_bin(dec_list)
# b) BIN -> DEC,
#bin_to_dec(dec_list)
