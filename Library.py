class Book:                                                #Clase Libro
    def __init__(self,name,author,pages,gender,state="Disponible"):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender
        self.state = state

    
class Catalog:        
                                                  #Clase Catologo
    def __init__(self):
        self.catalogList = []

    def AddBook(self,book):
        self.catalogList.append(book)

    def DeleteBook(self,name):
        index = 0
        for book in self.catalogList:
            if book.name == name:
                self.catalogList.pop(index)
                break

    def ShowCatalog(self):
        for book in self.catalogList:
            if book.state == "Disponible":
                print("Titulo: {0} Autor: {1} Genero: {2} Disponibilidad: {3}".format(book.name,book.author,book.gender,book.state))



class User:                                             #Clase Usuario
    def __init__(self,id,name,lastname,age):

        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.userBorrowebBooks = []
    
    def ShowBorrowedBooks(self):
        for i in self.userBorrowebBooks:
            print(i)

class load:                                          #Clase prestamo
    def __init__(self,book,user,dateInit,dateExit):
        self.book = book
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        self.borrowedBooks = []

    def LendBook(self,catalog):
        
        for book in catalog.catalogList:
            if book.name == self.book and book.state == "Disponible":
                register = "Libro: {0}, Persona: {1} {2}, Fecha de inicio: {3}, Fecha de termino: {4}".format(self.book,self.user[1],self.user[2],self.dateInit,self.dateExit)
                self.borrowedBooks.append(register)
                print(self.user)
                self.user.userBorrowebBooks.append(register)


    def ShowLendBook(self):
        for i in self.borrowedBooks:
            print(i)

#creo libro


catalogo = Catalog()
narnia = Book("narnia", "Kevin parra",190,"narrative")
harry = Book("harry el sucio poter","kevin parra",1000,"horror")
diabetin = Book("diabetin","satan",123,"horror")

catalogo.AddBook(narnia)
catalogo.AddBook(harry)
catalogo.AddBook(diabetin)

#catalogo.ShowCatalog()

catalogo.DeleteBook("narnia")


#Creando usuario

Kevin = ("21.566.366-4","Kevin","Parra",19)

#Creando Load

Kevin_load = load("diabetin",Kevin,"mayo 18 2023","mayo 23 2023")
Kevin_load.LendBook(catalogo)

Kevin_load.ShowLendBook()


Kevin.ShowBorrowedBooks()