
"""
ENUNCIADO

1. Tabla de multiplicar

Haz un programa que te pregunte el 
resultado de multiplicar dos números 
repetidamente, hasta que falles.
Entonces, indica el resultado correcto 
y cuándo aciertos seguidos has tenido.

Ayuda: hay que importar la librería 
random:
importe random
y para devolver un número entre 1 y 9:
número = random.randrange(1,10) 

"""

#escribe la soluncion aqui:
#SOLUCION



import random

fallo = False
aciertos = 0

while not fallo:
  n1 = random.randrange(1,10)
  n2 = random.randrange(1,10)
  mult = int(input(f"{n1} por {n2}? "))
  if mult != n1 * n2:
    print(f"incorrecto, es {n1*n2}")
    fallo = True
  else:
    aciertos += 1

print(f"{aciertos} aciertos seguidos!")


