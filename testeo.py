LIST_USERS = []

class Book:                                                #Clase Libro
    def __init__(self,id,name,author,pages,gender):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender
        self.state = "Disponible"

    
class Catalog:        
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
        self.userborrowedBooks= []
    
    def ShowBorrowedBooks(self):
        for books in self.userborrowedBooks:
            print(books)

    def ShowInformation(self):
        print("Id: ", self.id)
        print("Nombre: ", self.name, self.lastname)
        print("Edad: ", self.age)
        print("Libros Prestados ", self.userborrowedBooks)
        
class load:                                          #Clase prestamo
    def __init__(self,book,user,dateInit,dateExit):
        self.book = book
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        self.borrowedBooks = []
        

    def LendBook(self,catalog,user):
        
        for book in catalog.catalogList:
            if book.name == self.book and book.state == "Disponible":
                register = "Libro: {0}, Persona: {1} {2}, Fecha de inicio: {3}, Fecha de termino: {4}".format(self.book,self.user[1],self.user[2],self.dateInit,self.dateExit)
                self.borrowedBooks.append(register)

                

    def ShowLendBook(self):
        for i in self.borrowedBooks:
            print(i)


def Clean():
    print("\n")



def ShowUser():
    Clean()
    for i in LIST_USERS:
        print(i.id,i.name,i.lastname)

def GetId():
    return len(LIST_USERS)
    

def Welcome():
    print("Bienvenido")

def Options():
    Clean()
    print("1. Registrar Usuario")
    print("2. Crear Libro")
    print("3. Eliminar Libro")
    print("4. Prestar Libro")
    print("5. Devolver Libro")
    print("6. Ver libros disponibles")
    print("7. Ver historial de un usuario")
    print("8. Mostrar todos los usuarios")
    print("0. Salir")
    
def main():
    CATALOG = Catalog()
    Welcome()
    userOptions = 1
    while userOptions != 0:
        Options()
        userOptions = int(input("> "))
        if userOptions == 1:
            userId = GetId()
            userName = input("Nombre: ")
            aux = userName
            userLastname = input("Apellido: ")
            userAge = int(input("Edad: "))
    
            globals()[aux] = User(userId,userName,userLastname,userAge)
            
            LIST_USERS.append(globals()[aux])
            
            ShowUser()
            
        elif userOptions == 2:
            bookName = input("Nombre del libro: ")
            aux = bookName
            bookAuthor = input("Autor: ")
            bookPages = input("Paginas: ")
            bookGender = input("Genero: ")
            globals()[aux] = Book(bookName,bookAuthor,bookPages,bookGender)
            CATALOG.catalogList.append(globals()[aux])
            
        elif userOptions == 3:
            bookName = input("Nombre del libro: ")
            CATALOG.DeleteBook(bookName)
            
            
            
        
        elif userOptions == 6:
            CATALOG.ShowCatalog()
            
            
            
            
            
            
            
    
            

if __name__ == '__main__':
    main()
