
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
            print(flight)            

class FlightNumber:
    def __init__(self,flight,origin,destination,date,assignedAircraft,gate):
        self.flight = flight
        self.origin = origin
        self.destination = destination
        self.date = date
        self.assignedAircraft = assignedAircraft
        self.gate = gate
        self.reservationList = []

    def ShowAllPasagers(self):
        for reservation in self.reservationList:
            print(reservation)
        
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

    def MakeReservation(self):

        if self.seat[0][0] == "1":
            self.flight.reservationList.append({"Pasajero":self.passenger.name + " " + self.passenger.lastname,"Vuelo":self.flight.flight,"Origen":self.flight.origin,"Destino":self.flight.destination,"Fecha":self.flight.date,"Asiento":self.seat,"Estado":self.state})
                    

    def CancelReservation(self):
        self.flight.reservationList[0]["Estado"] = "Cancelado"
        #for flight in self.flight.reservationList:
            
        #    print(i)
    
    def ShowAllReservation(self):
        for passenger in self.flight.reservationList:
            print(passenger)

    
    
#COMENZAMOS


#Creacion de Aviones        
Avion1 = Airplane("Airbus A320",140)
Avion2 = Airplane("Boeing 737",230)
Avion3 = Airplane("Boeing 787 Dreamliner",2)

#creando vuelos a Avion1
Temuco_Santiago = FlightNumber("TM-2313","Temuco","Santiago","10:15 Sab.4 Nov.2023",Avion1,"A24")
Santiago_Arica = FlightNumber("SAN-7131","Santiago","Arica","12:15 Sab.5 Nov.2023",Avion1,"C12")

#Creando vuelos a Avion2
BuenosAires_Caracas = FlightNumber("BN-6541","Buenos Aires","Caracas","11:30 Mie.9 Oct.2024",Avion2,"B09")
Lima_Santiago = FlightNumber("LIM-7589","Lima","Santiago","18:00 Lun.23 Dic.2023",Avion2,"B23")

#Creando vuelos a Avion3
LaPaz_Cordoba = FlightNumber("Paz-4234","LaPaz","Cordoba","13:00 Mie.12 Nov.2023",Avion3,"D24")
Cordoba_Santiago = FlightNumber("Cor-9215","Cordoba","Santiago","14:00 Mar.27 Nov.2023",Avion3,"F12")


#Asignado vuelos a Avion1
Avion1.AddFlight(Temuco_Santiago)
Avion1.AddFlight(Santiago_Arica)

#Asigando vuelos a Avion2
Avion2.AddFlight(BuenosAires_Caracas)
Avion2.AddFlight(Lima_Santiago)

#Asignado vuelos a Avion3
Avion3.AddFlight(LaPaz_Cordoba)
Avion3.AddFlight(Cordoba_Santiago)

Avion1.AddFlight(Temuco_Santiago)
Avion1.AddFlight(Santiago_Arica)


#Pasajeros
Kevin_Parra = Passenger("Kevin","Parra","A1234567")
Brayan_Torres = Passenger("Brayan","Torres","C3213415")
Lucas_Mendez = Passenger("Lucas","Mendez","F5890321")
Sofia_Ramirez = Passenger("Sofia","Ramirez","B7128495")


#Reservando Pasajeros para el avion 1
Kevin_Parra_Reservacion = Reservation(Kevin_Parra,Temuco_Santiago,"7C","Activo")
Brayan_Torres_Reservacion = Reservation(Brayan_Torres,Temuco_Santiago,"1B","Activo")
Kevin_Parra_Reservacion.MakeReservation()
Brayan_Torres_Reservacion.MakeReservation()

#Mostrando reservacion solo del avion1
Brayan_Torres_Reservacion.ShowAllReservation()

#Reservando pasajetos para el avion3
Lucas_Mendez_Reservacion = Reservation(Lucas_Mendez,LaPaz_Cordoba,"1A","Activo")
Sofia_Ramirez_Reservacion = Reservation(Sofia_Ramirez,LaPaz_Cordoba,"2B","Activo")
Lucas_Mendez_Reservacion.MakeReservation()
Sofia_Ramirez_Reservacion.MakeReservation()

#Mostrando reservacion solo del avion3
Sofia_Ramirez_Reservacion.ShowAllReservation()
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
Temuco_Santiago.ShowAllPasagers()