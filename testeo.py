
class avion:
    class vuelo:
        class pasajero:
            class reservas:
                def __init__(self,pasajero,vuelo,estado):
                    self.pasajero=pasajero
                    self.vuelo=vuelo
                    self.estado=estado
            def __init__(self,nombre,numero_pasaporte,lista_vuelos_reservados,reservacion):
                self.nombre=nombre
                self.numero_p=numero_pasaporte
                self.lista_v_r=lista_vuelos_reservados
                self.reserva=self.pasajero(reservacion)
        def __init__(self,origen,destino,fecha,hora,avion_asignado,lista_de_reservas,pasajero):
            self.origen=origen
            self.destino=destino
            self.fecha=fecha
            self.hora=hora
            self.avion_a=avion_asignado
            self.lista_de_reservas=lista_de_reservas
            self.pasajero=self.reserva(pasajero)
    def __init__(self,modelo,asientos,numero_vuelo):
        self.modelo=modelo
        self.asientos=asientos
        self.numero_vuelo=self.avion_a(numero_vuelo)
