
#Class and OOP

#class Dog:
#   def bark(self):
#      print( "Woof")

# Object
#myobject= Dog
#myobject.bark()

#class Vehicle:
#   def Toyota(self):
#        print("4 Runner")

# Object
# myCar = Vehicle()
# myCar.Toyota()


#class Computer:
#    def Dell(self):
#        print(" Modedl 2025")

# Object
#mycomputer = Computer()
#mycomputer.Dell()


#class Money:
#    def USD(self):
#        print("1 USD = 65 AFN")

#ObjMoney = Money()
#ObjMoney.USD()


# --init-- Method  and attributes

# class Vehicle:
#     def __init__(self, Name, Model, Color,):
#         self.Name = Name
#         self.Model = Model
#         self.Color = Color
    
#     def Car(self):
#         print(f"{self.Name} Model {self.Model} Color {self.Color}")

# # #Object
# # myCar = Vehicle("Toyota", " 2026", " Black")
# # myCar.Car()


# class Organization:
#     def __init__(self, Name, offices, DateofEstablished,):
#        self. Name = Name
#        self. offices = offices
#        self. DateofEstablished = DateofEstablished
    
#     def NGO(self):
#         print(f"Name {self.Name} Provincial offices {self.offices} DateofEstablished {self.DateofEstablished}")

# Org = Organization ("CHA Organization", "Marar, Zabul, Herat and Kandahar", " 1987-10-10")
# Org.NGO()


# inner Class and type of Variables in Class

# Basic Class 

# class Person:
#     def greet(self):
#         print(" Hello, Welcome to the inner class and type varialble lesson")

# p = Person ()
# p.greet ()

# Class with __init__ and attributes 

# class Car:
#     def __init__(self, Name, model):
#         self.Name = Name
#         self.model = model
#     def info(self):
#         print(f"This car is {self.Name} and the modle is {self.model}")

# c = Car("Toyotota", 2025)
# c.info()

# class Book:
#     def __init__(self, Name, Author, Yearofpulication):
#         self.Name = Name
#         self.Author = Author 
#         self.Yearofpulication = Yearofpulication

#     def info(self):
#         print(f" The Name of the book is {self.Name} the Author is {self.Author} and the Year of Pulicaiotn is {self.Yearofpulication}")
    
# b = Book(" Masnawe", "Baghlani", "2000-10-10")
# b.info()


class Sport:
    def __init__(self, Name, City, Totalplayer):
        self.Name = Name
        self.City = City
        self.Totalplayer = Totalplayer

    def team(self):
        print(f" The team name is {self.Name} , The City is {self.City} and the Total are {self.Totalplayer}")
    
s = Sport ("Tawana Volyball", "Herat", "6 Players")
s.team()











# polymorphism 

# import math

# class TrigFunction:
#     def calculate(self, x):
#         pass   


# class Sine(TrigFunction):
#     def calculate(self, x):
#         return math.sin(x)


# class Cosine(TrigFunction):
#     def calculate(self, x):
#         return math.cos(x)


# class Tangent(TrigFunction):
#     def calculate(self, x):
#         return math.tan(x)

# class Cotangent(TrigFunction):
#     def calculate(self, x):
#         return 1 / math.tan(x)

# # Polymorphism in action
# functions = [Sine(), Cosine(), Tangent(), Cotangent()]

# angle = math.radians(90)   

# for func in functions:
#     print(func.calculate(angle))
