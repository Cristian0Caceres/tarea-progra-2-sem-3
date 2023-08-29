#!/usr/bin/env python3

import random

from colorama import Fore, init

init(autoreset=True)

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
        self.assigned = ASIGNED
        self.origin = ORIGIN
        self.destination = DEST
        self.date = DATE
        self.reservationList = []
        self.name = self.randID()


    # Se genera una ID random, origen + destino + 4 numeros random
    def randID(self):
        temp = ""
        for i in range(4):
            temp += str(random.randint(0, 9))
        return f"{self.origin[:2]}{self.destination[:2]}{temp}"
    
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
def main():
    print("Hola ")