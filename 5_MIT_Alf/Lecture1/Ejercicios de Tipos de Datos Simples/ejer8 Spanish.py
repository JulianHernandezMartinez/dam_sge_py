dividendo = int(input("Dividendo : "))
divisor = int(input("Divisor : "))
resto = dividendo%divisor
cociente = int(dividendo/divisor) # truncates float values
print(str(dividendo)+" entre "+str(divisor)+" da un cociente de "+str(cociente)+" y un resto de "+str(resto))
# print(f'{dividendo} entre {divisor} da un cociente de {cociente} y un resto de {resto}')

# Another choices / options
import math
quotient = math.floor(dividendo/divisor)
print(f'{dividendo} dividido por {divisor} da un cociente de {cociente} y un resto de {resto}')
