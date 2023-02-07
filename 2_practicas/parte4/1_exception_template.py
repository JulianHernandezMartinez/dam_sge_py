from time import sleep

""" tratamiento de excepcion 

El siguiente codigo pide dos intervalos en segundos
y establece esperas con arreglo a esos intervalos.

ENUNCIADO
Tienes que modificarlo para que se puedan
interrumpir la primera espera con CTRL-C y a 
la vez, que se saquen por consola el 
segundo en el que se ha interrumpido e 
informacion de la excepcion que la ha 
esa interrupcion Ctrl-C
 
"""

intervalo1 = int(input('Segundos en la primera espera (3-10)?'))
intervalo2 = int(input('Segundos en la segunda espera (3-10)?'))

#primera espera
print(f'lanzada la primera espera con {intervalo1} segundos')
sleep(intervalo1)
print(f'finalizada la primera espera')
#segunda  espera
print(f'lanzada la segunda espera con {intervalo2} segundos')
sleep(intervalo2)
print(f'finalizada la segunda espera')


"""SOLUCION Modifica este codigo"""


intervalo1 = int(input('Segundos en la primera espera (3-10)?'))
intervalo2 = int(input('Segundos en la segunda espera (3-10)?'))

#primera espera
print(f'lanzada la primera espera con {intervalo1} segundos')
sleep(intervalo1)
print(f'finalizada la primera espera')
#segunda  espera
print(f'lanzada la segunda espera con {intervalo2} segundos')
sleep(intervalo2)
print(f'finalizada la segunda espera')



""" Derivada 2 """
"""Implementa la SOLUCION  con llamada a funcion"""
""" Una llamada a una funcion esperaycuenta que este protegida"""

intervalo1 = int(input('Segundos en la primera espera (3-10)?'))
intervalo2 = int(input('Segundos en la segunda espera (3-10)?'))

#primera espera
#primera espera
print(f'lanzada la primera espera con {intervalo1} segundos')
sleep(intervalo1)
print(f'finalizada la priera espera')
#segunda  espera
print(f'lanzada la segunda espera con {intervalo2} segundos')
sleep(intervalo2)
print(f'finalizada la segunda espera')


