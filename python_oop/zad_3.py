# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:18:24 2023

@author: m-gru
"""


class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Property: {self.address}\n"
            f"Area: {self.area} sq. m\nRooms: {self.rooms}\n"
            f"Price: ${self.price}"
            )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House: {self.address}\n"
            f"Area: {self.area} sq. m\nRooms: {self.rooms}\n"
            f"Price: ${self.price}\nPlot size: {self.plot} sq. m"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat: {self.address}\n"
            f"Area: {self.area} sq. m\nRooms: {self.rooms}\n"
            f"Price: ${self.price}\nFloor: {self.floor}"
        )


# Tworzenie obiektów klasy House i Flat
house = House(area=150, rooms=5, price=300000,
              address="Wojewodzka 15", plot=500)
flat = Flat(area=80, rooms=3, price=150000, address="456 Mariacka 20", floor=2)

# Wyświetlanie obiektów
print(house)
print("\n-----------------\n")
print(flat)
