
class Airplane:
    def __init__(self,model,seatNumber):
        self.model = model
        self.seatNumber = seatNumber
        self.destinations = []
    
    def ShowAirplane(self):
        print("Modelo del Avion: {0} Numero de asientos: {1} ".format(self.model,self.seatNumber))    
    
    def AddFlight(self,flight):
        self.destinations.append({"Origen":flight.origin,"Destino":flight.destination,"Fecha":flight.date,"Avion":flight.assignedAircraft.model},)
        
    def ShowAllflights(self):
        for flight in self.destinations:
            print("Origen = " + flight["Origen"] + " | " + "Destino = " + flight["Destino"] + " | " + "Fecha = " + flight["Fecha"] + " | " + "Avion = " + flight["Avion"])
            
class FlightNumber:
    def __init__(self,origin,destination,date,assignedAircraft):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.assignedAircraft = assignedAircraft
        self.reservationList = []
        
class Passenger:
    def __init__(self,name,lastname,passportNumber,seat):
        self.name = name
        self.lastname = lastname
        self.passportNumber = passportNumber
        self.seat = seat
            
class Reservation:
    def __init__(self,passenger,flight,state):
        self.passenger = passenger
        self.flight = flight
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
                if self.passenger.seat[0][0] == "A":
                    seat = self.passenger.seat + " " + self.passenger.name + " " + self.passenger.lastname
                    self.reservations[0].append(seat)

    
    def ShowAllReservation(self):
        print(self.passenger.name + " " +self.passenger.lastname)

#Creacion de Aviones        
Avion1 = Airplane("Airbus A320",140)
Avion2 = Airplane("Boeing 737",230)
Avion3 = Airplane("Boeing 787 Dreamliner",240)

#Describre los aviones
Avion1.ShowAirplane()

#creando vuelos
Temuco_Santiago = FlightNumber("Temuco","Santiago","10:15 Sab.4 Nov.2023",Avion1)
Santiago_Arica = FlightNumber("Santiago","Arica","12:15 Sab.5 Nov.2023",Avion1)
Avion1.AddFlight(Temuco_Santiago)
Avion1.AddFlight(Santiago_Arica)
Avion1.ShowAllflights()

#Pasajero
Kevin_Parra = Passenger("Kevin","Parra","A1234567","A23")

#Reservar vuelo
Kevin_Parra_Reservation = Reservation(Kevin_Parra,Temuco_Santiago,"Activo")
Kevin_Parra_Reservation.MakeReservation()

Kevin_Parra_Reservation.ShowAllReservation()




    