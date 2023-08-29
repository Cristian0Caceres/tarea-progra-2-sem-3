#!/usr/bin/env python3

from src.classes import *
from src.randomFunc import *


def CreateVuelo():
    print("Ingrese el origen:")
    dato1 = input(">")
    print("\n")

    print("Ingrese el destino:")
    dato2 = input(">")
    print("\n")

    print("Ingrese el mes (en número, ej: 1 para enero, 2 para febrero, etc.):")
    dato4 = int(input(">"))
    while dato4 < 1 or dato4 > 12:
        print("Mes inválido. Ingrese un número entre 1 y 12:")
        dato4 = int(input(">"))
    print("\n")

    print("Ingrese el día:")
    dato3 = int(input(">"))

    # Validación de días segun el mes
    while dato3 < 1 or dato3 > 31:
        print("Día inválido. Ingrese un número entre 1 y 31:")
        dato3 = int(input(">"))

    # Validación específica para febrero
    if dato4 == 2 and dato3 > 29:
        print("Febrero tiene máximo 29 días. Ingrese un día válido:")
        dato3 = int(input(">"))

    if dato4 in [4, 6, 9, 11] and dato3 > 30:
        print("Este mes tiene máximo 30 días. Ingrese un día válido:")
        dato3 = int(input(">"))
    print("\n")



def GenerateVuelo():    
    maxVuelos = 10
    OrigenList = ["Nueva York", "Los Ángeles", "Londres", "París", "Tokio", "Roma", "Sídney", "Toronto", "Pekín", "Río de Janeiro"]
    DestinoList = ["San Francisco", "Chicago", "Berlín", "Barcelona", "Osaka", "Florencia", "Melbourne", "Montreal", "Shanghái", "Buenos Aires"]
    
    for i in range(maxVuelos):
        Variable = f"Vuelo_{i+1}"
        
        Avion  = random.choice(ListaAviones)
        Origen = random.choice(OrigenList)
        Destino = random.choice(DestinoList)
        Fecha = GenerateDate()
        Fecha = f"{Fecha[0]} {Fecha[1]}, {Fecha[2]}:{Fecha[3]}"
        globals()[Variable] = Flight(Avion, Origen, Destino, Fecha)
        ListaVuelos.append(globals()[Variable])

def GenerateAvion():
    maxAviones = 10
    for i in range(maxAviones):
        Variable = f"Avion_{i+1}"
        globals()[Variable] = Airplane()
        ListaAviones.append(globals()[Variable])

def VerVuelos():
    switch = True
    print("----------------------------------------")
    print("            Vuelos Disponibles          ")
    print("----------------------------------------")
    for i in range(len(ListaVuelos)):
        temp = ListaVuelos[i]
        name = temp.name
        origin = temp.origin
        destination = temp.destination
        date = temp.date
        if switch:
            print(Fore.LIGHTBLACK_EX + f"{origin} a {destination}, {date}")
            switch = False
        else:
            print(Fore.LIGHTCYAN_EX + f"{origin} a {destination}, {date}")
            switch = True
    print("----------------------------------------")

def main():    
    # Generamos una serie de aviones
    GenerateAvion()
    # Creacion de Vuelos con destinos aleatorios y les asignamos aviones aleatorios
    GenerateVuelo()
    # Funcion para ver todos los vuelos disponibles
    VerVuelos()


def ClearTerm():
    for i in range(100):
        print("\n")


if __name__ == "__main__":
    ListaVuelos = []
    ListaAviones = []

    main()
