#!/usr/bin/env python3



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

import random
import string
from colorama import Fore, init

class Airplane:
    def __init__(self):
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
        
        
        self.MODEL = self.GenerateAirplaneModel() # Retorna un modelo aleatorio
        self.SEATSNUM = self.GetAirplaneSeatNum() # Retorna los asientos disponibles
        
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
        
        for i in range(len(self.SEATSMAP)): # 15 arrays = 15 filas de asiento
            for j in range(len(self.SEATSMAP[i])):  # Dentro de cada array hay 6 asientos + 1 el pasillo
                if self.SEATSMAP[i][j] == "" or self.SEATSMAP[i][j] == " X ":   # Si es el pasillo o si está ocupado
                    continue
                else:
                    seatCounter += 1

        self.SEATSNUM = seatCounter

        return self.SEATSNUM

    def GetAirplaneMap(self):
        print("")
        print("-------------------------------------")
        print("              Asientos               ")
        print("-------------------------------------")
        for i in range(len(self.SEATSMAP)): #Leemos el mapa de asientos para saber que tan largo es
            for j in range(len(self.SEATSMAP[i])): # Iteramos sobre cada array dentro del array del mapa
                if self.SEATSMAP[i][j] == "": # Si el array está vacio entonces no printea nada, esto quiere decir que es el pasillo
                    print("  ",end="") # Printeamos nada    
                
                elif self.SEATSMAP[i][j] == " X ":  # X -> Asiento ocupado
                    print(f"{Fore.RED}[{self.SEATSMAP[i][j]}] ",end="")
                
                else:
                    print(f"{Fore.GREEN}[{self.SEATSMAP[i][j]}] ",end="" ) # Printea el asiento "[A0], [A1], [A2]..."
            print("\n", end="")
        

    # Funcion para actualizar un asiento y que ahora esté ocupado
    def UpdateReserved(self, seat):
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == seat:
                    self.SEATSMAP[i][j] = " X "
                else:
                    continue

    def UpdateCanceled(self, seat, seatPos):
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if (i, j) == seatPos:
                    self.SEATSMAP[i][j] = seat
                else:
                    continue

    def CalculateSeat(self, seat):   #Funcion para retornar la posicion del asiento
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == seat:
                    return (i, j)
                else:
                    continue

    def CheckSeat(self, seat): # Funcion para verificar si el asiento es valido
        for i in range(len(self.SEATSMAP)):
            for j in range(len(self.SEATSMAP[i])):
                if self.SEATSMAP[i][j] == seat and self.SEATSMAP[i][j] != " X ":
                    return True
                else:
                    continue
        return False


class Flight:
    def __init__(self, ASIGNED, ORIGIN, DEST, DATE):
        self.name = GenerateID(ORIGIN, DEST)
        self.assigned = ASIGNED
        self.origin = ORIGIN
        self.destination = DEST
        self.date = DATE
        self.reservationList = []

    def showPassengers(self):
        print("--------------------------------")
        print(f"    Pasajeros - {self.name}    ")
        print("--------------------------------")
        for i in range(len(self.reservationList)):
            name = self.reservationList[i].passenger.name
            rut = self.reservationList[i].passenger.passportNumber
            asiento = self.reservationList[i].seat
            print(f"{name}, {rut} - {asiento}")

class Reservation:
    def __init__(self, seat, passengerClass, flightClass):
        self.seat = seat
        self.passenger = passengerClass
        self.flight = flightClass
        self.state = "Reservado"
        self.seat_POS = flightClass.assigned.CalculateSeat(seat)        

class Passenger:
    def __init__(self, NAME, LASTNAME, PASSPORT):
        self.name = f"{NAME} {LASTNAME}"
        self.passportNumber = PASSPORT
        self.reservationsList = []

    def addReservation(self, RESERVATION):
        RESERVATION.flight.assigned.UpdateReserved(RESERVATION.seat)
        RESERVATION.flight.reservationList.append(RESERVATION)
        self.reservationsList.append(RESERVATION)# Añadimos la reservacion a la lista

    def delReservation(self, RESERVATION):
        RESERVATION.flight.assigned.UpdateCanceled(RESERVATION.seat, RESERVATION.seat_POS)
        RESERVATION.flight.reservationList.remove(RESERVATION)
        self.reservationsList.remove(RESERVATION)# Quitamos la reservacion de la lista

    def PassengerInfo(self):
        print("---------------------------------------------")
        print("           Informacion del Pasajero          ")
        print("---------------------------------------------")
        print("Nombre:          " + self.name)
        print("Pasaporte:       " + self.passportNumber)
        self.ShowAllReservation()
        
        
    def ShowAllReservation(self):
        print("---------------------------------------------")
        print("                Reservaciones                ")
        print("---------------------------------------------")
        for i in self.reservationsList:
            # Informacion del vuelo 
            state = i.state
            seat = i.seat
            flight = i.flight
            name = flight.name
            origin = flight.origin
            destination = flight.destination
            date = flight.date
            # Informacion del avion 
            flight = flight.assigned
            flight_name = flight.MODEL
            print("ID:              " + name)
            print("Asiento:         " + seat)
            print("Avion:           " + flight_name)
            print("Estado:          " + state)
            print("Origen:          " + origin)
            print("Destino:         " + destination)
            print("Fecha:           " + date)
            
            print("---------------------------------------------")

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
#           Chulchul Villarrica - ChVi1234
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