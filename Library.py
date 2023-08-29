class Book:                                                #Clase Libro
    def __init__(self,name,author,pages,gender):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender

    
class Catalog:        
                                                  #Clase Catologo
    def __init__(self):
        self.catalog = []

    def ShowCatalog():
        for i in self.genders:
            print(i)


class User:                                             #Clase Usuario
    def __init__(self,id,user,lastname,age):

        self.id = id
        self.user = user
        self.lastname = lastname
        self.age = age

class load:                                          #Clase prestamo
    def __init__(self,book,user,dateInit,dateExit):
        self.book = book
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        

#creo libro

narnia = Book("narnia", "Kevin parra",190,"narrative")
