""" Classes and Objetc review"""

"""Si elimino el comentario # de la 
siguiente linea un error  aparece

TypeError: object of type 'int' has no len()

"""

# print(len(5)) 

"""" muestra que 5 es un objeto del tipo
"int" , y que no tiene len() podemos
conocer sus funciones asociadas con dir(5)"""

print(dir(5))

# Metodo (Method) es una funcion de un objeto 
# de una clase de Python

"""__add__ y __and__ son metodos del objeto 
"int" mientras __len__() no es un metodo de
"int" """

print(dir("test")) # muestr metodos del objeto string "test"

print()
print("test".__len__()) # 4  para mostras las tripas
print(len("test")) #4 opcion elegante para usar
print('test'.islower(),'abdc'.replace('a','b')) # True, "bbcd"

# OOBJETO
# Objeto es una coleccion de datos(variables) y metodos
# (funciones) que operan en esos datos.
# An object is a collection of data (variables) and 
# methods that operate on that data

# Objects can be used to model many real-life concepts 
# and situations

"""CLASES son los "mapas" que definen los tipos
y los metodos que pueden soportar"""

# CLASS = A class is the blueprint for one 
# or more objects

# algunas clases nativas
print(type('a')) # <class 'str'>
print(type(1)) # <class 'int'>
print(type(True)) # <class 'bool'>

# Creando las clases Python

# Clase "Car"
class Car:
    speed = 0
    started = False
    def start(self):
        self.started = True
        print("Car started, let's ride!")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
    def stop(self):
        self.speed = 0
        print('Halting')

car=Car()
print(car.increase_speed(10))
print(car.start())
print(car.increase_speed(40))

# self parameter in python classes
# hace referencia a la propia instancia
# creada del objeto, y permite hacer 
# referencia a si mismo

"""
When we call a method on a Python object, 
Python automatically fills in the first 
variable, which we call self by convention.

This first variable is a reference to the 
object itself, hence its name.

We can use this variable to reference 
other instance variables and functions 
of this object, like self.speed and 
self.start()

So only inside the Python class 
definition, we use self to reference 
variables that are part of the instance. 

To modify the started variable that’s 
part of our class, we use self.started 
and not just started. 

By using self, it’s made abundantly 
clear that we are operating on a 
variable that’s part of this instance 
and not some other variable that is 
defined outside of the object and 
happens to have the same name.

"""
""""""
#Creating multiple Python objets
car1=Car()
car2=Car()

# id() buit-in method shows the unique Id of each car object
print(id(car1))
print(id(car2))

car1.start() # Car started, let's ride!
car1.increase_speed(10) #increase speed 10 km/hour and print Vrooooom!
print(car1.speed) # 10 .- car1 speed is now 10
print(car2.speed) # 0 car2  speed is Cero, not even started YET

#Inheritance
""" si vemos con dirCar) los metodos de Car, 
ademas de los definidos . start, stop, 
.increase_speed... cuenta con otros muchos
empezando por __class__, y __init__ """

print(dir(Car)) # Metodos de Car, ademas de los definidos 



