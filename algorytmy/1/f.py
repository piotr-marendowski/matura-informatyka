dlugosc = int(input("Podaj dlugosc ciagu: "))
# iteracyjne obliczanie wartości liczb Fibonacciego
# fibonacci = 1 1 2 3 5 8... element to suma dwoch poprzednich
# dlatego zaczynamy od dwoch jedynek
# i pierwsza liczba to bedzie ta druga
# a druga liczba to ich suma i wypisujemy ja
def fibonacci_it(n):
    liczba1, liczba2 = 1, 1

    for i in range(1, n + 1):
        print(liczba1)
        liczba1, liczba2 = liczba2, liczba1 + liczba2


fibonacci_it(dlugosc)
print("")

# rekurencyjne obliczanie wartości liczb Fibonacciego
# jesli n < 3 to sa te pierwsze
# chyba to dziala tak ze idzie ciagle w dol tj. uzywa tylko jedynek dla dwoch poprzednich
# wyrazow ciagu i je dodaje np. 4 wyraz to 3 czyli (1 + 1) + (1)
def fibonacci_re(n):
    if n < 3:
        return 1

    return fibonacci_re(n - 1) + fibonacci_re(n - 2)


for i in range(0, dlugosc):
    print(fibonacci_re(i+1))
