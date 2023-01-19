#Funciones
a_string = "hola caracola" #cadena de caracteres

a_integer_number = 123
a_float_number = 12.3456
a_boolean_true = True
a_boolean_false = False
a_new_boolean_true = True
a_new_boolean_false = False
verdadomentira = True

print()
print('FUNCIONES def nombre_funcion(arg1,..argx  una funcion que suma dos numeros')
print('identation automatica con 4 espacios para identificar el bloque de codigo')

def add_numbers(a=0,b=0):
    return(a+b)  # 4 spacios para identificar el bloque de codigo de la funcion add_numbers establecidos automaticamente por un IDE decente

print(add_numbers(a_integer_number,a_float_number)) #135.3456 la suma de integer_number = 123 y a_float_number = 12.3456 
print(add_numbers()) # zero
print(add_numbers(12)) # 12

def add_numbers_and_print(a,b):
    print(a+b)  # 4 spacios para identificar el bloque de codigo de la funcion add_numbers establecidos automaticamente por un IDE decente

add_numbers_and_print(a_integer_number,a_float_number)

def saludador_opcional(name):
    if name.startswith('J'):
        # We don't greet people with common names :p
        return
    
    print('Hola',name)
saludador_opcional('Julian')  #Salida con retorno vacio, nombre empieza por J
saludador_opcional('Petra')   #Salida con retorno con saludo
saludador_opcional('julian')   #Salida con retorno con saludo, pues empieza por j -minuscula-Case Sensitive

# ejemplo de funciones con parametros y valores por defecto, que entran en juego si no se les asigna un valor

def bienvenida(nombre ='aprendiz',localizacion ="el tutorial"):
    print('Bienvenid@', nombre, 'a', localizacion)

bienvenida()
bienvenida(nombre='Maria')
bienvenida(nombre='Miguel',localizacion='este increible playground de Python')


print('pueden retornar multiples resultados, se recomienda que se usen dataclasses para obtenerlos')
print('las dataclasses se han agregado para evitar "misstypes"pueden retornar multiples resultados, se recomienda que se usen dataclasses para obtenerlos')

# @dataclass
from dataclasses import dataclass
@dataclass
class Card:
    rank: str
    suit: str
    
card1 = Card("Q", "hearts")
card2 = Card("Q", "hearts")
print(card1 == card2)
# True
print(card1.rank)
# 'Q'
print(card1)
# Card(rank='Q', suit='hearts')
card2.rank="Y"
print(card1==card2)
#False
print(card2)
# Card(rank='Y', suit='hearts')
