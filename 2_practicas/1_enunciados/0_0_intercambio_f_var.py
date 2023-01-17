# Este primer ejercicio es de ejemplo
# Se incluye la parte comentada con "#"
# Y la solución
# 
# Enunciado
#
# haz un programa que pida dos numeros X e Y y que los intercambie
# y presente una salida del tipo "número 1 es Y , número 2 es X"
#
# 
# Escribe tu solucion aqui: 
#
# SOLUCION

num1 = int(input("número 1? "))
num2 = int(input("número 2? "))

temp = num1
num1 = num2
num2 = temp

print(f"número 1 es {num1}, número 2 es {num2}")
