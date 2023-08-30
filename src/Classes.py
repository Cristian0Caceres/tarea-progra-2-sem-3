#!/usr/bin/env python3

import random
import string
from colorama import Fore, init

init(autoreset=True)

#  ________________________________________
# / Una clase es un conjunto de atributos  \
# | que se pueden usar para crear varios   |
# | objetos individuales, los atributos    |
# | definen los objetos, así como un      |
# | conjunto de comportamientos (Funciones |
# \ o metodos)                             /
#  ----------------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||

class Airplane:
    def __init__(self):
        self.MODEL = self.GenerateAirplaneModel()
        self.SEATSMAP = [
        ["A01","B01","C01","","D01","E01","I01"],
        ["A02","B02","C02","","D02","E02","I02"],
        ["A03","B03","C03","","D03","E03","I03"],
        ["A04","B04","C04","","D04","E04","I04"],
        ["A05","B05","C05","","D05","E05","I05"],
        ["A06","B06","C06","","D06","E06","I06"],
        ["A07","B07","C07","","D07","E07","I07"],
        ["A08","B08","C08","","D08","E08","I08"],
        ["A09","B09","C09","","D09","E09","I09"],
        ["A10","B10","C10","","D10","E10","I10"],
        ["A11","B11","C11","","D11","E11","I11"],
        ["A12","B12","C12","","D12","E12","I12"],
        ["A13","B13","C13","","D13","E13","I13"],
        ["A14","B14","C14","","D14","E14","I14"],
        ["A15","B15","C15","","D15","E15","I15"]
        ]
        
        self.SEATSNUM = self.GetAirplaneSeatNum()
        
    def GenerateAirplaneModel(self):
        Models = [
            "Boeing 737", "Airbus A320", "Boeing 777",
            "Airbus A380", "Dreamliner",
            "Embraer E195","Bombardier CRJ700",
            "Sukhoi Superjet 100"
            ]
        return random.choice(Models)

    def GetAirplaneSeatNum(self):
        seatCounter = 0
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == "" or self.SEATSMAP[i][j] == " X ":
                    continue
                else:
                    seatCounter += 1

        self.SEATSNUM = seatCounter

        return self.SEATSNUM

    def GetAirplaneMap(self):
        print("")
        print("-------------------------------------")
        print("        Asientos Disponibles         ")
        print("-------------------------------------")
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == "":
                    print("  ",end="")
                elif self.SEATSMAP[i][j] == " X ":
                    print(f"{Fore.RED}[{self.SEATSMAP[i][j]}] ",end="")
                else:
                    print(f"[{self.SEATSMAP[i][j]}] ",end="" )
            print("\n", end="")
    def UpdateReserved(self, seat):
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == seat:
                    self.SEATSMAP[i][j] = " X "
                    
class Flight:
    def __init__(self, ASIGNED, ORIGIN, DEST, DATE):
        self.name = GenerateID(ORIGIN, DEST)
        self.assigned = ASIGNED
        self.origin = ORIGIN
        self.destination = DEST
        self.date = DATE
        self.reservationList = []

class Passenger:
    def __init__(self, NAME, LASTNAME, PASSPORT):
        self.name = f"{NAME} {LASTNAME}"
        self.passportNumber = PASSPORT
        self.reservationsList = []
    
    def addReservation(self, RES):
        self.reservationsList.append(RES)
        seat = RES.number
        RES.flight.assigned.UpdateReserved(seat)

    def ShowAllReservation(self):
        print("---------------------------------------------")
        print("                Reservaciones                ")
        print("---------------------------------------------")
        for i in self.reservationsList:
            # Informacion del vuelo 
            temp = i.flight
            state = i.state
            name = temp.name
            origin = temp.origin
            destination = temp.destination
            date = temp.date
            # Informacion del avion 
            flight = temp.assigned
            flight_name = flight.MODEL
            print("ID:              " + name)
            print("Avion:           " + flight_name)
            print("Estado:          " + state)
            print("Origen:          " + origin)
            print("Destino:         " + destination)
            print("Fecha:           " + date)
            
            print("---------------------------------------------")

    def PassengerInfo(self):
        print("---------------------------------------------")
        print("           Informacion del Pasajero          ")
        print("---------------------------------------------")
        print("Nombre:          " + self.name)
        print("Pasaporte:       " + self.passportNumber)
        self.ShowAllReservation()


class Reservation:
    def __init__(self, seat, passengerClass, flightClass):
        self.number = seat
        self.passenger = passengerClass
        self.flight = flightClass
        self.state = "Reservado"

    def CancelReservation(self):
        self.state = "Cancelado"




#*  _______________________
#* < Funciones Principales >
#*  -----------------------
#*         \   ^__^
#*          \  (oo)\_______
#*             (__)\       )\/\
#*                 ||----w |
#*                 ||     ||


def GenerateID(param1=None, param2=None):
    temp = ""
    temp2 = ""
    if param1 is None and param2 is None:
        temp2 = ''.join(random.choices(string.ascii_lowercase, k=4))
        return f"{temp2}{temp}"
    else:   
        for i in range(4):
            temp += str(random.randint(0, 9)) 
        return f"{param1[:2]}{param2[:2]}{temp}"

def ClasifMonth(mes):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    return meses.get(mes, "Mes inválido")
    
def GenerateDate():
    mes = random.randint(1, 12)
    
    if mes in [4, 6, 9, 11]:  # Meses con 30 días
        dia = random.randint(1, 30)
    elif mes == 2:  # Febrero
        dia = random.randint(1, 28)
    else:  # Meses con 31 días
        dia = random.randint(1, 31)
    
    hora = random.randint(0, 23)
    minutos = random.randint(0, 59)
    
    mes = ClasifMonth(mes)
    
    return mes, dia, hora, minutos

def CrearVuelo():
    print("")
    print("Ingrese el origen:")
    dato1 = input(">")

    print("")
    print("Ingrese el destino:")
    dato2 = input(">")

    print("")
    print("Ingrese el mes (en número, ej: 1 para enero, 2 para febrero, etc.):")
    dato4 = int(input(">"))
    while dato4 < 1 or dato4 > 12:
        print(Fore.RED + "Mes inválido. Ingrese un número entre 1 y 12:")
        dato4 = int(input(">"))
    dato4 = ClasifMonth(dato4)

    print("")
    print("Ingrese el día:")
    dato3 = int(input(">"))

    # Validación de días segun el mes
    while dato3 < 1 or dato3 > 31:
        print(Fore.RED + "Día inválido. Ingrese un número entre 1 y 31:")
        dato3 = int(input(">"))

        # Validación específica para febrero
        if dato4 == 2 and dato3 > 29:
            print(Fore.RED + "Febrero tiene máximo 29 días. Ingrese un día válido:")
            dato3 = int(input(">"))

        if dato4 in [4, 6, 9, 11] and dato3 > 30:
            print(Fore.RED + "Este mes tiene máximo 30 días. Ingrese un día válido:")
            dato3 = int(input(">"))
    
    hora_valida = False
    print("")
    print("Ingrese una hora en formato hh:mm (de 00:00 a 23:59):")
    while not hora_valida:
        dato5 = input(">")
        try:
            hora, minutos = map(int, dato5.split(":"))
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                hora_valida = True
            else:
                print(Fore.RED + "Hora inválida. Ingrese una hora válida.")
        except ValueError:
            print(Fore.RED + "Formato incorrecto. Ingrese la hora en el formato hh:mm.")
    print("")
    print("Seleccione un avión:")
    for i in range(len(ListaAviones)):
        print(f"{i+1}. {ListaAviones[i].MODEL}") #Listamos los aviones para elegir uno para el vuelo
    i = int(input(">"))
    
    
    print("")
    print(Fore.GREEN + f"Vuelo creado exitosamente: \nAvion:{ListaAviones[i-1].MODEL}  \nOrigen: {dato1} \nDestino: {dato2} \nFecha: {dato4} del {dato3} \nHora: {dato5}")

    Vuelo = GenerateID(dato1, dato2)
    globals()[Vuelo] = Flight(ListaAviones[i-1], dato1, dato2, f"{dato4} {dato3}, {dato5}")
    ListaVuelos.append(globals()[Vuelo])


def CrearPassenger():
    print("")
    print("Ingresa tu primer nombre: ")
    name = input(">")
    name = name.replace(" ", "")
    
    while name == "":
        print(Fore.LIGHTRED_EX + "Ingresa tu primer nombre: ")
        name = input(">")
        name = name.replace(" ", "")
    
    print("")
    print("Ingresa tu Apellido Paterno: ")
    Lastname = input(">")
    Lastname = Lastname.replace(" ", "")
    
    while Lastname == "":
        print(Fore.LIGHTRED_EX + "Ingresa tu Apellido Paterno")
        Lastname = input(">")
        Lastname = Lastname.replace(" ", "")
        
    print("")
    print("Ingresa tu Rut/Pasaporte (Sin puntos, sin guión, ni el digito verificador): ")
    doc = input(">")
    doc = doc.replace(" ", "")   
    
    Temp = GenerateID(name, Lastname)
    globals()[Temp] = Passenger(name, Lastname, doc)

# def ReservarVuelo():
#     print("")
#     print("Ingresa tu Rut/Pasaporte (Sin puntos, sin guión, ni el digito verificador): ")
#     doc = input(">")
#     doc = doc.replace(" ", "")
#     for i in range(len(ListaPasajeros)):
#         if ListaPasajeros[i].passportNumber == doc:
            
            
# def CancelarReservacion():
#     print("vuelo cancelado xd")
    

def GenerateVuelo():
    maxVuelos = 10
    OrigenList = ["Santiago","Valparaíso","Concepción","Antofagasta",
              "Puerto Montt","La Serena","Iquique","Arica",
              "Punta Arenas","Calama","Temuco","Rancagua",
              "Viña del Mar","Valdivia","Copiapó"]

    DestinoList = ["Valparaíso","Arica","Puerto Montt","La Serena",
               "Calama","Concepción","Iquique",
               "Punta Arenas","Viña del Mar", "Villarrica", "La casa del Profe Elliott", "Campus Norte"]

    for i in range(maxVuelos):
        Avion  = random.choice(ListaAviones)
        Origen = random.choice(OrigenList)
        Destino = random.choice(DestinoList)
        Fecha = GenerateDate()
        Fecha = f"{Fecha[0]} {Fecha[1]}, {Fecha[2]}:{Fecha[3]}"
        Vuelo = GenerateID(Origen, Destino)
        globals()[Vuelo] = Flight(Avion, Origen, Destino, Fecha)
        ListaVuelos.append(globals()[Vuelo])

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
    Bucle = True
    while Bucle:
        print("Seleccione una opcion para realizar: ")
        print("1. Crear un vuelo")
        print("2. Reservar un vuelo")
        print("3. Cancelar reservación")
        print("4. Opcion 4")
        print("5. Opcion 5")
        print("6. Ver todos los vuelos")
        print("7. Salir")
        try:    
            choice = int(input("> "))
            if choice == 1:
                CrearVuelo()
            elif choice == 2:
                ReservarVuelo()
            elif choice == 3:
                CancelarReservacion()
            elif choice == 4:
                print("opcion4")
            elif choice == 5:
                print("opcion5")
            elif choice == 6:
                VerVuelos()
            elif choice == 7:
                Bucle = False
        except Exception as r:
            print("Por favor ingrese una opcion valida :)")
            # print(r)

ListaVuelos = []
ListaAviones = []
ListaPasajeros = []