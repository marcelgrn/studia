# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:08:06 2023

@author: m-gru
"""


def czy_parzysta(liczba):
    return liczba % 2 == 0


# Użycie funkcji
liczba = int(input("Podaj liczbę: "))
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
