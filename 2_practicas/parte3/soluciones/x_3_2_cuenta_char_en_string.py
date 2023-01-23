# ENUNCIADO DE LA PRACTICA
#
# Pregunta por un caracter 
# a contar y cuenta el numero de  
# veces que aparece en una palabra o frase.
# 
# RESTRICCION
# no se puede utilizar el metodo .count
# 
# VALORABLE
# La simplicidad y brevedad del codigo
#
# SOLUCION
#


char=input('caracter a contar?')
a = input('palabra o frase en la que contar el caracter?')

count = 0
for c in range(len(a)):    
    if a[c] == char:
        count += 1
print(count)

print(a.count(char))