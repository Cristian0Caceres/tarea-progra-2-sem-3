class Book:                                                #Clase Libro
    def init(self,id,name,author,pages,gender):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.gender = gender

class Catalog:                                          #Clase Catologo

    def init(self,gender):
        self.gender = gender
        self.TerrorBooks = []
        self.RomanticBooks = []

class User:                                             #Clase Usuario
    def init(self,id,user,lastname,age):

        self.id = id
        self.user = user
        self.lastname = lastname
        self.age = age

class load:                                          #Clase prestamo
    def init(self,book,user,dateInit,dateExit):
        self.book = book
        self.user = user
        self.dateInit = dateInit
        self.dateExit = dateExit
        