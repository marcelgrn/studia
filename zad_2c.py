# -*- coding: utf-8 -*-
"""
16.10
zad 2c
"""


def wyswietl_parzyste_elementy(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)


# Tworzenie listy z liczbami
lista_liczb = list(range(1, 11))

# Wywołanie funkcji
wyswietl_parzyste_elementy(lista_liczb)
