# Crea un programa que guarde las puntuaciones de los jugadores del Tetris. 
# El programa debe pedir la y puntuación de tres jugadores,

# jug1 = "Rosa"
# jug2 = "Alberto"
# jug3 = "Alejandro"

# Tiene que ordenar las puntuaciones en formato podio (es decir de forma descendente). 
# Por último, mostrará por pantalla el podio final.

# 1. Ichigo– 1220
# 2. Rukia – 1198
# 3. Kisuke - 850

jug1 = "Rosa"
jug2 = "Alberto"
jug3 = "Alejandro"

p1 = int(input(f"{jug1}? "))
p2 = int(input(f"{jug2}? "))
p3 = int(input(f"{jug3}? "))

if p1 >= p2 and p1 >= p3:
    if p2 >= p3:
        nom1 = jug1; nom2 = jug2; nom3 = jug3
        punt1 = p1; punt2 = p2; punt3 = p3
    else:
        nom1 = jug1; nom2 = jug3; nom3 = jug2
        punt1 = p1; punt2 = p3; punt3 = p2
elif p2 >= p1 and p2 >= p3:
    if p1 >= p3:
        nom1 = jug2; nom2 = jug1; nom3 = jug3
        punt1 = p2; punt2 = p1; punt3 = p3
    else:
        nom1 = jug2; nom2 = jug3; nom3 = jug1
        punt1 = p2; punt2 = p3; punt3 = p1
elif p3 >= p1 and p3 >= p1:
    if p1 >= p2:
        nom1 = jug3; nom2 = jug1; nom3 = jug2
        punt1 = p3; punt2 = p1; punt3 = p2
    else:
        nom1 = jug3; nom2 = jug2; nom3 = jug1
        punt1 = p3; punt2 = p2; punt3 = p1

print(f"1. {nom1} - {punt1}")
print(f"2. {nom2} - {punt2}")
print(f"3. {nom3} - {punt3}")
