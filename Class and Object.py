
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
    def __init__(self, Name, Model):
        self.Name = Name
        self.Model = Model
    
    def Car(self):
        print(f"{self.Name} Model {self.Model}")

#Object
myCar = Vehicle("Toyota", " 2026")
myCar.Car()