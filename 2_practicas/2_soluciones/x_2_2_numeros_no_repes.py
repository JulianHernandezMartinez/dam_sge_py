
"""
ENUNCIADO

2. Lista sin repetidos

Haz un programa que te pida repetidamente
números y los guarde.

a) Si el número es cero, que termine 
el programa. 
b) Si no existe, que lo añada a una 
lista y muestre la nueva lista.
c) Si existe, que diga que ya existe 
y no la añada.

"""



#escribe la soluncion aqui:
#SOLUCION



list = []
acabar = False

while not acabar:
  number = int(input("nuevo numero (0 para finalizar)? "))
  if number == 0:
    acabar = True
  elif number in list:
    print("el numero ya existe")
  else:
    list.append(number)
    print(list)

print("adios!")

