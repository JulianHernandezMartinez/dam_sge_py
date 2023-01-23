"""
ENUNCIADO

4. Haz un programa que adivine un número 
que generas con un random ("número").
El programa pide que introduzcas un 
número ("entrada") entre A y B, inicialmente 1 y 99.
Si aciertas, le felicitas y acabas.

Tienes que ir cambiando A y B según lo que 
introduzca el usuario para ir reduciendo 
el intervalo.

(imagine que el número es el 20)
entre 1 y 99? 45
es más pequeño
entre 1 y 44? 13
es mayor
entre 14 y 44? 20
exacto! """

#escribe la soluncion aqui:
#SOLUCION

import random

min = 1
max = 99
nombre = random.randrange(1, 100)
found = False
while not found:
    guess = int(input(f"entre {min} y {max}? "))
    if guess == nombre:
        found = True
    elif guess < nombre:
        print(f"más grande que {guess}")
        if guess >= min:
            min = guess+1
    elif guess > nombre:
        print(f"más pequeño que {guess}")
        if guess <= max:
            max = guess-1
print(f"correcto!")

# 4. Fes un programa que endevini un nombre que generes amb un random ("nombre").
# El programa demana que introdueixis un nombre ("entrada") entre A i B, inicialment 1 i 99.
# Si l'encertes, el felicites i acabes.
# Has d'anar canviant A i B segons el que introdueixi l'usuari per anar reduïnt l'interval.
