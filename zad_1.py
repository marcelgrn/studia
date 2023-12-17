# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:02:46 2023

@author: m-gru
"""
"""
6.11
"""


def przywitanie(name, surname):
    return f"Cześć {name} {surname}!"


# Użycie funkcji
name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")

wynik_przywitania = przywitanie(name, surname)
print(wynik_przywitania)
