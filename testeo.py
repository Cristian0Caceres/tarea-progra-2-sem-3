class Book:                                                #Clase Libro
    def __init__(self,id,name,author,pages,gender,state="Disponible"):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender
        self.state = state

    
class Catalog:        
    def __init__(self):
        self.catalogList = [
    [0, "La casa de los espíritus", "Isabel Allende", 368, "Narrativo de terror", "Chile", "Disponible"],
    [1, "Los detectives salvajes", "Roberto Bolaño", 648, "Narrativo de terror", "Chile", "No Disponible"],
    [2, "2666", "Roberto Bolaño", 912, "Narrativo de terror", "Chile", "Disponible"],
    [3, "La ciudad de los prodigios", "Eduardo Mendoza", 408, "Narrativo de terror", "Chile", "Disponible"],
    [4, "La muerte de Artemio Cruz", "Carlos Fuentes", 291, "Narrativo de terror", "Chile", "Disponible"]
            ]

    def AddBook(self,book):
        self.catalogList.append(book)

    def DeleteBook(self,id):
        index = 0
        for book in self.catalogList:
            if book[0] == int(id):
                self.catalogList.pop(index)
                break   
            index += 1

    def ShowCatalog(self):
        for book in self.catalogList:
            print("Id " + str(book[0]) + " Titulo: "+ book[1] + " Autor: " + book[2] + " Paginas: " + str(book[3]) + " Genero: " + book[4] + " Estado " +book[5])

    def ShowAvailableCatalog(self):
        for book in self.catalogList:
            if book[6] == "Disponible":
                print("Id " + str(book[0]) + " Titulo: "+ book[1] + " Autor: " + book[2] + " Paginas: " + str(book[3]) + " Genero: " + book[4] + " Estado " +book[5])

    def ShowNotAvailableCatalog(self):
        for book in self.catalogList:
            if book[6] == "No Disponible":
                print("Id " + str(book[0]) + " Titulo: "+ book[1] + " Autor: " + book[2] + " Paginas: " + str(book[3]) + " Genero: " + book[4] + " Estado " +book[5])


        
class User:                                             #Clase Usuario
    def __init__(self,id,name,lastname,age):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.userborrowedBooks= []
    
    def ShowBorrowedBooks(self):
        print("the usser borrow: ")
        for books in self.userborrowedBooks:
            print(books)

    def ShowInformation(self):
        print("Id: ", self.id)
        print("Nombre: ", self.name, self.lastname)
        print("Edad: ", self.age)
        print("Libros Prestados ", self.userborrowedBooks)
        
class Load:                                          #Clase prestamo
    def __init__(self,bookId,user,dateInit,dateExit):
        self.bookId = bookId
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        self.borrowedBooks = []
        

    def LendBook(self,catalog):
        
        for book in catalog.catalogList:
            if book[6] == "Disponible":
                if book[0] ==  int(self.bookId):
                    ide = len(self.borrowedBooks)
                    book[6] = "No Disponible"
                    print(catalog)
                    self.borrowedBooks.append(["Id: " + str(ide),"Nombre: " + book[1], "Autor: " + book[2],"Persona: " + self.user])
                
    def ReturnBook(self,catalog):
        print("entro")
        print(self.bookId,catalog.catalogList)
        
        

        

        

    def ShowLendBook(self):
        for i in self.borrowedBooks:
            print(i)


LIST_USERS = [

]
CATALOG = Catalog()

def Clean():
    print("\n")

def ShowUser():
    Clean()
    for user in LIST_USERS:
        print(user.id,user.name,user.lastname,user.age)

def GetUserMemory(userId):
    for user in LIST_USERS:
        if user.id == userId:
            return user


def GetIdBooks():
    return len(CATALOG.catalogList)

def GetIdUsers():
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
    print("9. Ver libros")
    print("0. Salir")
    
def Usserbooks():
    Clean()
    if len(LIST_USERS) == 0:
        print("please register a usser first to continue")
    else:
        print("seleccione un usuario")
        option_u=input("escriba el nombre de usuario para continuar: ")
        for user in  LIST_USERS:
            if option_u == user:
                print(f"el usuario tiene en su poder {LIST_USERS[user].userborrowedBooks}")

def main():
    Welcome()
    userOptions = 1
    while userOptions != 0:
        Options()
        userOptions = int(input("> "))
        if userOptions == 1:
            userId = GetIdUsers()
            userName = input("Nombre: ")
            aux = userName
            userLastname = input("Apellido: ")
            userAge = int(input("Edad: "))
            globals()[aux] = User(userId,userName,userLastname,userAge)
            LIST_USERS.append(globals()[aux])
            print(LIST_USERS)
            ShowUser()
        elif userOptions == 2:
            bookId = GetIdBooks()
            bookName = input("Nombre del libro: ")
            aux = bookName
            bookAuthor = input("Autor: ")
            bookPages = input("Paginas: ")
            bookGender = input("Genero: ")
            globals()[aux] = Book(bookId,bookName,bookAuthor,bookPages,bookGender)
            CATALOG.catalogList.append([bookId,globals()[aux].name,globals()[aux].author,globals()[aux].pages,globals()[aux].gender,"Disponible"])
            
        elif userOptions == 3:
            CATALOG.ShowCatalog()
            bookId = input("Id del libro: ")
            CATALOG.DeleteBook(bookId)
            
        elif userOptions == 4:
            ShowUser()
            UserId = int(input("ID: "))
            CATALOG.ShowAvailableCatalog()
            userMemorySpace = GetUserMemory(UserId)
            BookId = input("Book Id: ")
            dateInit = input("Fecha de inicio ejemplo(18 oct 2023): ")
            dateExit = input("Fecha de regreso ejemplo(25 oct 2023)")
            aux = userMemorySpace
            globals()[aux] = Load(BookId,userMemorySpace.name,dateInit,dateExit)
            
            globals()[aux].LendBook(CATALOG)
            globals()[aux].ShowLendBook()
            
        elif userOptions == 5:
            ShowUser()
            UserId = int(input("ID: "))
            CATALOG.ShowNotAvailableCatalog()
            userMemorySpace = GetUserMemory(UserId)
            print(userMemorySpace)
            userId = input("Book Id: ")
            aux = userMemorySpace
            globals()[aux].ReturnBook(CATALOG)


            
            
        elif userOptions== 8:
            ShowUser()
        elif userOptions == 9:
            CATALOG.ShowCatalog()
        elif userOptions == 7:
            ShowUser()
            Usserbooks()
        

if __name__ == '__main__':
    main()



