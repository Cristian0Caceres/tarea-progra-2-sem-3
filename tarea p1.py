
class vuelo:
    class avion:
        def __init__(self,modelo_de_avion,cantidad_asientos,codigo_identificador):
            self.modelo_de_avion=modelo_de_avion
            self.cantidad_asientos=cantidad_asientos
            self.IDnumero=codigo_identificador

    def __init__(self,origen,destino,fecha,hora,codigo_identificador):
        self.origen=origen
        self.destino=destino
        self.fecha=fecha
        self.hora=hora
        self.avion= self.avion("boing 737 max 8","210", codigo_identificador)
mi_vuelo=vuelo("argentina","chile","2023-08-24","23:00","FLT342")

print(mi_vuelo.destino)