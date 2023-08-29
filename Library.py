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

    def AddBook(self,book):
        self.catalog.append(book)


    def ShowCatalog(self):
        for book in self.catalog:
            print("Titulo: {0} Autor: {1} Genero {2}".format(book.name,book.author,book.gender))

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


catalogo = Catalog()
narnia = Book("narnia", "Kevin parra",190,"narrative")
harry = Book("harry el sucio poter","kevin parra",1000,"horror")
locuras_pyeter_pkaer = Book("diabetin","satan",123,"horror")

catalogo.AddBook(narnia)
catalogo.AddBook(harry)
catalogo.AddBook(locuras_pyeter_pkaer)


catalogo.ShowCatalog()


