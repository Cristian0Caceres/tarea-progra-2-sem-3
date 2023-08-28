class libro:
    def __init__(self,Author,Gender,Date_C,Pages,Publisher):
        self.author=Author
        self.gender=Gender
        self.Date_C=Date_C
        self.pages=Pages
        self.publisher=Publisher
class usuario:
    def __init__(self,prestamos,ussername,):
        self.prestamos=prestamos
        self.usuario=ussername
class prestamos:
    def __init__(self,prestamos,fecha_i,fecha_t):
        self.prestamos=prestamos
        self.fechainicio=fecha_i
        self.fechatermino=fecha_t
