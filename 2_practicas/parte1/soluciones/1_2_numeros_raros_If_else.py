
""" fuente hackerrank.com 

 TAREA
 Dado un número n entero realizado las 
 acciones condicionales siguientes:

 Si n es impar imprimir “Raro”
 Si n es par y está incluido entre el 
 rango 2 a 5 imprimir “No raro”
 Si n es par y está incluido entre el 
 rango 6 a 20 imprimir “Raro”
 Si n es par y mayor que 20 imprimir “No raro”

 FORMATO DE ENTRADA
 Una línea simple conteniendo un número entero positivo, n

 LIMITACIONES
 1<=n<=100

 FORMATO DE SALIDA
 Imprime”Raro” en el caso de un número raro o de lo contrario imprime “No raro”

 MUESTRA DE ENTRADA
 3

 MUESTRA DE SALIDA
 Raro

 EXPLICACION
 n=3
 n es impar y los números impares son Raros
 
 Escribe tu solucion aqui: 

 SOLUCION

"""

# if __name__ == '__main__':
#     n = int(input().strip())

n = int(input("numero? "))


if (n>0 and n<101):
    if ((n%2==1) or (n>5 and n<21)):
        print('Raro, in english weird')
    else:
        print("No Raro, in english Not Weird")
else:
    print('Number should be among 1 and 100')

# fuente hackerrank.com 

# TAREA
# Dado un número n entero realizado las acciones condicionales siguientes:

# Si n es impar imprimir “Raro”
# Si n es par y está incluido entre el rango 2 a 5 imprimir “No raro”
# Si n es par y está incluido entre el rango 6 a 20 imprimir “Raro”
# Si n es par y mayor que 20 imprimir “No raro”

# FORMATO DE ENTRADA
# Una línea simple conteniendo un número entero positivo, n

# LIMITACIONES
# 1<=n<=100

# FORMATO DE SALIDA
# Imprime”Raro” en el caso de un número raro o de lo contrario imprime “No raro”

# MUESTRA DE ENTRADA
# 3

# MUESTRA DE SALIDA
# Raro

# EXPLICACION
# n=3
# n es impar y los números impares son Raros

