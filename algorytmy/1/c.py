# Liczba doskonala to taka ktorej dzielniki sie dodaja w nia sama
# oczywiscie musi byc wieksza od 1
# i lecimy prosze ja ciebie bardzo od poczatku do niej samej (jebac optymalizacje)
# jesli znajdziemy dzielnik (czyli np. 10 / 5 = bez reszty), to dodajemy do listy
# potem porownujemy czy ta liczba rowna sie sumie tych jej dzielnikow
def doskonala(liczba):
    dzielniki = []

    if liczba > 1:
        for i in range(1, liczba):
            if liczba % i == 0:
                dzielniki.append(i)

        if liczba == sum(dzielniki):
            return True

    return False


print(f"6: {doskonala(6)}\n")

liczby = [1, 3, 5, 6, 12, 25, 28, 34, 496]

for liczba in liczby:
    print(f"{liczba}: {doskonala(liczba)}")
