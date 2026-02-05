
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

#Object
#myCar = Vehicle()
#myCar.Toyota()


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

class Vehicle:
    def __init__(self, Name, Model, Color,):
        self.Name = Name
        self.Model = Model
        self.Color = Color
    
    def Car(self):
        print(f"{self.Name} Model {self.Model} Color {self.Color}")

#Object
myCar = Vehicle("Toyota", " 2026", " Black")
myCar.Car()



class Organization:
    def __init__(self, Name, offices, DateofEstablished,):
       self. Name = Name
       self. offices = offices
       self. DateofEstablished = DateofEstablished
    
    def NGO(self):
        print(f"Name {self.Name} Provincial offices {self.offices} DateofEstablished {self.DateofEstablished}")

Org = Organization ("CHA Organization", "Marar, Zabul, Herat and Kandahar", " 1987-10-10")
Org.NGO()