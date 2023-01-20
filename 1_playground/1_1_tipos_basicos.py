print('TIPOS BASICOS y AUTOTIPADOS')
print('\n')

a_string = "hola caracola" #cadena de caracteres
print(a_string)
print('el string "',a_string,'" se puede \nconsiderar un array o lista \nde caracteres. OJO (PROBLEMILLA - ERROR,\ncon espacios)')
print(a_string[0]) # caracter del indice 0 ('h') de la cadena "hola caracola"

print("\nla funcion f'string_x {} permite \nformar o formatear frases y resolver \nel problemilla de espacios\n")
frase =f'el PROBLEMA-ERROR de los espacios en:\nel string "{a_string}" se puede \nya CORREGIDO!!, sin espacios \ngracias a f-funcion'
print(frase)

print('\nla funcion len(string), o len(x)\n')

length_of_a_string = len(a_string)
print(length_of_a_string) # imprime la longitud de la cadena "hola caracola"

a_integer_number = 123
a_float_number = 12.3456
a_boolean_true = True
a_boolean_false = False
a_new_boolean_true = True
a_new_boolean_false = False
verdadomentira = True

print({a_integer_number},{a_float_number},{a_boolean_true},{a_boolean_false})
print(a_integer_number,a_float_number,a_boolean_true,a_boolean_false)


print('\nFuncion type() obtiene la clase/tipo de una variable \n')

# Funcion type() restorna el tipo asignado a una variable
print(type(a_string))
print(type(a_float_number))
print(type(verdadomentira))


print('... y parecia buena idea pero...')
print('....no lo era \n ¡muerte al "autotipado! \n ¡vivan los constructores de tipos! \n')

print('CONSTRUCTORES/ASIGNADORES/CONVERSORES de TIPOS \n')

x = str("Hello World") # str --> usar el constructor asegura que el tipo de esa variable es str
print("""x = str('Hello World') \n""")
print(x)
print(type(x))
x.center

z=1j
print(z)
print(type(z))

x = str("Hello World") # str
x = int(20) #int 	
x = float(20.5)#float 	
x = complex(1j)#complex 	
x = list(("apple", "banana", "cherry"))#list 	
x = tuple(("apple", "banana", "cherry"))#tuple 	
x = range(6)#range 	
x = dict(name="John", age=36)#dict 	
x = set(("apple", "banana", "cherry"))#set 	
x = frozenset(("apple", "banana", "cherry"))#frozenset 	
x = bool(5)#bool 	
x = bytes(5)#bytes 	
x = bytearray(5)#bytearray 	
x = memoryview(bytes(5)) #memoryview

print('\nFIN DE TIPOS BASICOS Y FUNCIONES BASICAS\n')

# para empezar a jugar con entradas  y salidas descomenta las dos lineas siguientes
dato =float(1.4567)
print(dato)
print(type(dato))
dato = input("introduce un dato, e.g. 1.4567?") # solicita una palabra por el default input
print(dato)
print(type(dato))
print('todo lo que se recoge es por defecto "string"')

