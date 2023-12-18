# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:15:26 2023

@author: m-gru
"""


def polacz_usun_poteguj(lista1, lista2):
    # Łączenie list
    polaczona_lista = lista1 + lista2
    # Usuwanie duplikatów
    unikalne_elementy = list(set(polaczona_lista))
    # Potęgowanie
    potegi = [x**3 for x in unikalne_elementy]
    return potegi


# Przykładowe użycie funkcji
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

wynik = polacz_usun_poteguj(lista1, lista2)
print("Wynik działania funkcji:", wynik)
