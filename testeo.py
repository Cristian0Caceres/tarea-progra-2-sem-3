class libro:
    def __init__(self,Author,Gender,Date_C,Pages,Publisher,nombre):
        self.author=Author
        self.gender=Gender
        self.Date_C=Date_C
        self.pages=Pages
        self.publisher=Publisher
        self.nombre=nombre
    def genero(self):
        print(f"el genero del libro es {self.gender}")
class prestamo:
    def __init__(self,prestamos,fecha_i,fecha_t,libro):
        self.prestamo=prestamos
        self.fechainicio=fecha_i
        self.fechatermino=fecha_t
        self.libro=libro
class usuario:
    def __init__(self,ussername):
        self.prestamo= []
        self.usuario=ussername
    def Addprestamo(self):
        self.prestamo.append({"prestamos":prestamo.prestamo,"fecha_i":prestamo.fechainicio,"fecha_t":prestamo.fecha_t,"libro":prestamo.libro})
class catalogo:
    def __init__(self,libro,cantidad,prestamos):
        self.prestamo = prestamos
        self.cantidad=cantidad
        self.libro=libro

libro1=libro("tadeus manus","terror","14/03/2022","234","lapilopes","las aventuras de paco")
libro2=libro("paco cabezas","fantasia","28/08/2023","40","tartarus company","alimac_leblanc")
libro3=libro("luan vazques","misterio","02/12/2021","345","pandoria")
libro4=libro("natalia cáceres","policias","31/11/2004","222","bnjiboi")

usuario1=usuario("luci")
usuario2=usuario("angello")
usuario3=usuario("luis")



