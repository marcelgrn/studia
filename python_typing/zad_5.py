# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:13:30 2023

@author: m-gru
"""


def sprawdz_obecnosc_wartosci(lista, wartosc):
    return wartosc in lista


# Przykładowe użycie funkcji
moja_lista = [1, 2, 3, 4, 5]
wartosc_do_sprawdzenia = int(input("Podaj wartość do sprawdzenia: "))

wynik = sprawdz_obecnosc_wartosci(moja_lista, wartosc_do_sprawdzenia)

if wynik:
    print(f"Lista zawiera wartość {wartosc_do_sprawdzenia}.")
else:
    print(f"Lista nie zawiera wartości {wartosc_do_sprawdzenia}.")
