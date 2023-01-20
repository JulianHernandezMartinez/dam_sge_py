"""

ENUNCIADO

Crea un programa en Python 
que genere, mediante una FUNCION,
las tablas de multiplicar, para 
imprimirlas por pantalla.

Las tablas se almacenaran en unas
listas, y se imprimiran en pantalla

Objetivo de aprendizaje

uso de funciones y recursividad 
con "for" y "range"s."

"""




def crea_tabla_mult(numero):
  numeros = []
  for i in range(1, 11):
    numeros.append(i * numero)
  return numeros

for i in range(1, 11):
  taula = crea_tabla_mult(i)
  print(f"{i}: {taula}")

