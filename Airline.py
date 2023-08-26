
class Airplane:
    def __init__(self,model,seatNumber):
        self.model = model
        self.seatNumber = seatNumber
        self.destinations = []
    
    def ShowAirplane(self):
        print("Modelo del Avion: {0} Numero de asientos: {1} ".format(self.model,self.seatNumber))    
    
    def AddFlight(self,flight):
        self.destinations.append({"vuelo":flight.flight,"Origen":flight.origin,"Destino":flight.destination,"Fecha":flight.date,"Puerta":flight.gate,"Avion":flight.assignedAircraft.model},)
        
    def ShowAllflights(self):
        for flight in self.destinations:
            print("Origen = " + flight["Origen"] + " | " + "Destino = " + flight["Destino"] + " | " + "Fecha = " + flight["Fecha"] + " | " + "Avion = " + flight["Avion"])
            
class FlightNumber:
    def __init__(self,flight,origin,destination,date,assignedAircraft,gate):
        self.flight = flight
        self.origin = origin
        self.destination = destination
        self.date = date
        self.assignedAircraft = assignedAircraft
        self.gate = gate
        self.reservationList = []
        
class Passenger:
    def __init__(self,name,lastname,passportNumber):
        self.name = name
        self.lastname = lastname
        self.passportNumber = passportNumber
            
class Reservation:
    def __init__(self,passenger,flight,seat,state):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.state = state
        self.reservations = [
            ["A"],
            ["B"],
            ["C"],
            ["D"],
            ["E"],
            ["F"]
        ]
        
    def MakeReservation(self):
        for i in range(0,1):
            for j in range(0,1):
                if self.seat[0][0] == "A":
                    print(self.flight.reservationList)
                    self.flight.reservationList.append({"Pasajero":self.passenger.name + " " + self.passenger.lastname,"Vuelo":self.flight.flight,"Origen":self.flight.origin,"Destino":self.flight.destination,"Fecha":self.flight.date,"Asiento":self.seat})
                    

    
    def ShowAllReservation(self):
        print(self)
        print("dentro")
        print(self.flight.reservationList)


#Creacion de Aviones        
Avion1 = Airplane("Airbus A320",140)
Avion2 = Airplane("Boeing 737",230)
Avion3 = Airplane("Boeing 787 Dreamliner",240)

#Describre los aviones
Avion1.ShowAirplane()

#creando vuelos
Temuco_Santiago = FlightNumber("TM-2313","Temuco","Santiago","10:15 Sab.4 Nov.2023",Avion1,"A24")
Santiago_Arica = FlightNumber("SAN-7131","Santiago","Arica","12:15 Sab.5 Nov.2023",Avion1,"C12")
Avion1.AddFlight(Temuco_Santiago)
Avion1.AddFlight(Santiago_Arica)
Avion1.ShowAllflights()

#Pasajero
Kevin_Parra = Passenger("Kevin","Parra","A1234567")
Brayan_Torres = Passenger("Brayan","Torres","C3213415")

#Reservar vuelo
Kevin_Parra_Reservation = Reservation(Kevin_Parra,Temuco_Santiago,"A21","Activo")
Kevin_Parra_Reservation.MakeReservation()

Brayan_Torres_Reservation = Reservation(Brayan_Torres,Temuco_Santiago,"A21","Activo")
Brayan_Torres_Reservation.MakeReservation()





    