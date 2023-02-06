a = 5.0
b = 2.3
c = a * b
print(c)


# asignacion
a = 1
print(a)
a = "mundo"
print(a)

#conversioness
numero = 4
flotant = 3.1
cadena = str(2.8)
print(cadena)
print(numero)
print(cadena == numero)
print(cadena == "2.8")
print(numero == 4)

numero2 = numero + float(cadena)
print(numero2)
numero2 = numero + round(float(cadena))
print(numero2)


# variable global en la funcion
# golbal keyword

x = "awesome"

def myfunc():
  global x   # emplea la variable x como global
  x = "fantastic" 

myfunc()

print("Python is " + x) # Python is fantastic