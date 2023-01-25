
"""Crea un programa que lee una 
cantidad por teclado y si es superior 
a 10.000 se le hace el 10% de descuento, 
de lo contrario únicamente le hace el 5%. 
El resultado es necesario que nos diga 
la cantidad descontada y la cantidad a pagar.




SOLUCION
"""

cantidad = int(input("cantidad? "))

if cantidad > 10000:
    descuento = 10
else:
    descuento = 5

descontado = cantidad * descuento/100
apagar = cantidad - descontado

print(f"descuento del {descuento}%, descontado {descontado}, a pagar {apagar}")