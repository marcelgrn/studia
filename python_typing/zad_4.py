# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:09:44 2023

@author: m-gru
"""


def sprawdz_sume(a, b, c):
    return a + b >= c


# Przykładowe użycie funkcji
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

wynik = sprawdz_sume(liczba1, liczba2, liczba3)

print(
    f"Czy suma pierwszych dwóch liczb jest większa lub równa trzeciej? {wynik}"
)
