# -*- coding: utf-8 -*-
"""
16.10
zad 2b
"""


def pomnoz_przez_dwa_a(lista_liczb):
    # Stworzenie pustej listy, w której będzie wynik końcowy
    wynik = []
    # Mnożenie liczb w liście
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# Przykładowa lista zawierająca 5 liczb
lista_liczb_a = [1, 2, 3, 4, 5]

# Wywołanie funkcji z listą liczb jako argumentem
wynik_a = pomnoz_przez_dwa_a(lista_liczb_a)

# Wyświetlenie wyniku
print(wynik_a)


##########################

def pomnoz_przez_dwa_b(lista_liczb):
    # Użyj listy składanej do pomnożenia każdego elementu przez 2
    wynik = [liczba * 2 for liczba in lista_liczb]
    # Zwróć zmodyfikowaną listę
    return wynik


# Przykładowa lista zawierająca 5 liczb
lista_liczb_b = [1, 2, 3, 4, 5]

# Wywołanie funkcji z listą liczb jako argumentem
wynik_b = pomnoz_przez_dwa_b(lista_liczb_b)

# Wyświetlenie wyniku
print(wynik_b)
