# -*- coding: utf-8 -*-
"""
16.10
zad 2d
"""


def wyswietl_co_drugi_element(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


# Utworzenie listy
lista_liczb = list(range(1, 11))

# Wywołanie funkcji
wyswietl_co_drugi_element(lista_liczb)
