"""
ENUNCIADO

3. Número máximo

a) Haz un programa que te pregunte 
primero cuántos números enteros 
introducirás. (e.g. 4 numeros)

b) Elprograma continua pidiendo nuemros
    numero 0?
    numero 1?
    numero 2?
    numero 3?
    y los guarda guárdalos en una lista.

c) Una vez introducidos, busca el 
mayor número y muéstralo.

No vale utilizar la función max() 
de Python.

Recuerda que puedes añadir elementos 
con append(elemento) y que puedes 
comprobar si un elemento existe en 
una lista con "elemento in lista".

"""

#escribe la soluncion aqui:
#SOLUCION

count = int(input("cuantos numeros? "))
list = []
for i in range(count):
    list.append(int(input(f"numero {i}? ")))

print(list)

found = False
for number in list:
    if not found:
        max = number
        found = True
    elif number > max:
        max = number

print(f"max is {max}")



