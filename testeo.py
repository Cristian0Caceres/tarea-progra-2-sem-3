class Book:                                                #Clase Libro
    def __init__(self,name,author,pages,gender):#creamos la clase book con los parametros de name author pages and gender 
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender
        self.state = "Disponible" #establecemos el estado inicial como disponible en cada libro 

    
class Catalog:        
                                                  #Clase Catologo
    def __init__(self):#creamos la clase de catalogo la cual tendra en su interior una lista como atrivuto 
        self.catalogList = []

    def AddBook(self,book):#creamos la siguiente funcion la cual añade libros a la lista dentro de catalogo
        self.catalogList.append(book)

    def DeleteBook(self,name):#la siguiente funcion se utilisara parra eliminar los libros dentro del catalogo
        index = 0
        for book in self.catalogList:
            if book.name == name:
                self.catalogList.pop(index)
                break

    def ShowCatalog(self):#la siguiente funcion se usa para mostrar los elementos en el interior del catalog 
        for book in self.catalogList:
            if book.state == "Disponible":
                print("Titulo: {0} Autor: {1} Genero: {2} Disponibilidad: {3}".format(book.name,book.author,book.gender,book.state))



class User:                                             #Clase Usuario
    def __init__(self,id,name,lastname,age):#creamos la clase de usuarios la cual tiene id , name , lastname , age
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.userborrowedBooks= []
    
    def ShowBorrowedBooks(self):#la funcionalidad de esta funcion recae en el mostrar los libros prestados 
        for books in self.userborrowedBooks:
            print(books)

    def ShowInformation(self):#la siguiente funcion se centra en mostrar  la informacion del usuario
        print("Id: ", self.id)
        print("Nombre: ", self.name, self.lastname)
        print("Edad: ", self.age)
        print("Libros Prestados ", self.userborrowedBooks)
        
class lend:                                          #Clase prestamo
    def __init__(self,book,user,dateInit,dateExit):#creamos la clase lend con los siguientes datos book usser date init date exit y una lista para almacenar los libros prestados
        self.book = book
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        self.borrowedBooks = []

    def LendBook(self,catalog,user):#la siguiente funcion consiste en agregar los libros prestados a la lista de libros prestados dentro de la clase lend
        
        for book in catalog.catalogList:
            if book.name == self.book and book.state == "Disponible":
                register = "Libro: {0}, Persona: {1} {2}, Fecha de inicio: {3}, Fecha de termino: {4}".format(self.book,self.user[1],self.user[2],self.dateInit,self.dateExit)
                self.borrowedBooks.append(register)

                

    def ShowLendBook(self):#la siguiente  funcion tiene la principal funcion de mostrar los libros
        for i in self.borrowedBooks:
            print(i)

def Welcome():
    print("Bienvenido")

def Options():
    print("1. Registrar Usuario")
    print("2. Crear Libro")
    print("3. Eliminar Libro")
    print("4. Prestar Libro")
    print("5. Devolver Libro")
    print("6. Ver libros disponibles")
    print("7. Ver historial de un usuario")
    print("0. Salir")
    
def main():
    CATALOG = Catalog()
    Welcome()
    userOptions = 1
    while userOptions != 0:
        Options()
        userOptions = int(input("> "))
        if userOptions == 1:
            userId = input("Id: ")
            userName = input("Nombre: ")
            aux = userName
            userLastname = input("Apellido: ")
            userAge = int(input("Edad: "))
            
            globals()[aux] = User(userId,userName,userLastname,userAge)
            
            globals()[aux].ShowInformation()
            
        elif userOptions == 2:
            bookName = input("Nombre del libro: ")
            aux = bookName
            bookAuthor = input("Autor: ")
            bookPages = input("Paginas: ")
            bookGender = input("Genero: ")
            globals()[aux] = Book(bookName,bookAuthor,bookPages,bookGender)
        
        elif userOptions == 3:
            bookName = input("Nombre del libro: ")
            CATALOG.DeleteBook
            
            
            
            
            
            
    
            

if __name__ == '__main__':
    main()



