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

print('CONSTRUCTORES/ASIGNADORES de TIPOS \n')

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

# YYY hasta aqui 1_tipos_basicos

print('\nFIN DE TIPOS BASICOS Y FUNCIONES BASICAS\n')

#tipos y estructuras de datos (tuplas, ranges, list, sets, dictionaries...)
print('\nTipos de estructuras de datos\n')

print('strings(array), TUPLAS, LISTAS, SETS, DICCIONARIOS, arrays  \n')

#TUPLAS('A','B', 1, 5, True)
#tuplas(), -->lists[] --> sets{} -->Dictionaries
print('TUPLAS() - como arrays INMUTABLES\n')

#tuplas,arrays inmutables
persona = ('Erika', 38, True)
print(persona) # tupla entre parentesis ()
name, age, registered = persona # permite asociar elementos a variables
print(name, age) # Erika 38
#sus elementos, caracteres, se pueden referenciar como elementos indexados de un array
print(persona[1], persona[2],'\n') # 38, True

# las tuplas no se pueden modificar 
# (son INMUTABLES), si se desean ampliar,
# es necesario crear una nueva tupla

print('\nla funcion len() NUEVAMENTE en string, tuplas, etc')
print('el operador "*" para desempaquetar, desplegar tuplas...\n')

t =(1,2,3, 'bici', 'coche', 'moto')
t1 = (*t,5,4,3) # '*' desempaqueta la tupla t, podemos crear t1, en base a t, pero no añadir sobre t
print(t1, 'la longitud de t es:', len(t), 'la longitud de t1 es:', len(t1))
print('la funcion str(t) convierte la tupla t en un string y ojo que le incluye los parentesis',str(t),'\n')

print('LISTAS - como arrays MUTABLES[] \n')

#lists, arrays mutables y pueden tener elementos repetidos
lista = [8,5,6,7,8,9]
l1=[0,]
print(lista)
l=list(t1) #list es un conversor de tupla en lista, conierte la tupla t1 en una lista l
print(l)

print('\n SETS - como arrays MUTABLES sin REPETIDOS{} \n')
# sets, arrays ORDENADOS y mutables, NO pueden tener elementos repetidos, 

s={9,7,5}
s1=set(t) #constructor/conversor de un set a partir de una tupla
s2=set(l) #constructor de un set a partir de una lista
s3=set()
print('a=',s1,'b=',set(t1),'c=', set(lista),'d=', set(l), 'e=',set(l)==set(t1), 'f=',set(),'g=',set(l1),'h=', s3)
print('\n')
# YYY hasta aqui 1_tipos_basicos_y_mas
# YYY hasta aqui 1_tipos_basicos_y_mas
print('OPERACIONES CON LISTAS')
print('\n')
# LISTS (Create, Sort, Append, Remove, And More)(arrays de elementos de todo tipo)

# Create
a_list_alphabet_and_numbers_and_booleams=['A','B','C','D',9,8,True,7,False,0]
a_new_list=['pedro', 'miguel', 23, 25]
a_empty_list=[]
# This is a list with three lists inside
game_board = [[], [], []]
a_nested_list=[['A','B','C'], ['D','E','F'], ['G','H','I']]

# Create with list() function
a_list_from_0_to_9=list(range(10))
a_list_from_1_to_9=list(range(1,10))
a_list_from_2_to_9_in_steps_of_2=list(range(2,10,2))
print(a_list_from_0_to_9)
print(a_list_from_1_to_9)
print(a_list_from_2_to_9_in_steps_of_2)
print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))

# Access - Accceder a_list[0] elements in lists[index desde 0 hasta len(gth)]

print(a_list_alphabet_and_numbers_and_booleams[2]=='C') #True el elemento del indez 2 es C
print(a_list_alphabet_and_numbers_and_booleams[-1]==0) #True el ultimo elemento de la lista es 0
print(a_list_alphabet_and_numbers_and_booleams[-2]==False) #True el penultimo elemento es False
print('el primer elemento de la lista, una lista', a_nested_list[0], 'el segundo elemento del segundo elemento', a_nested_list[1][1])

# Append - Añadir a una lista un elemento y SOLO uno
a_list_alphabet_and_numbers_and_booleams.append('H')
a_list_alphabet_and_numbers_and_booleams.append('True')
a_list_alphabet_and_numbers_and_booleams.append(123)

print(a_list_alphabet_and_numbers_and_booleams)

# Agregar listas con '+' y con .extend
a_newest_list = a_list_alphabet_and_numbers_and_booleams + a_new_list
a_brand_new_list = a_newest_list.extend(a_new_list)
print(a_newest_list)
print(a_brand_new_list) #ojo dara 'None'??
print(a_newest_list.extend(a_new_list)) #ojo dara 'None'??
print(a_newest_list.extend(a_newest_list)) # ojo dara 'None'?? recursivo...??

#extraer y eliminar elementos de la lista con .pop
a_list_flores=['rosa', 'margarita','clavel','tulipan']
print(a_list_flores.pop(), a_list_flores.pop(1), a_list_flores) #extrae el ultimo, y el del index =1, y queda con los elementos restantes

#eliminar elementos con del(list[])
del(a_list_flores[0]) # borramos la rosa
print(a_list_flores)

#remove specific value in a list, in this example, 20 and 'sal'
a_list_ingredients_and_quantities=['ajo','cebolla','pimiento','tomate','sal',20, 100, 50,750,3]
a_list_ingredients_and_quantities.remove(20)
a_list_ingredients_and_quantities.remove('sal')
print(a_list_ingredients_and_quantities)

#clear all elememts in a list
a_list_ingredients_and_quantities.clear()
print(a_list_ingredients_and_quantities)

a_list_ingredients_and_quantities.append('melocoton')
print(a_list_ingredients_and_quantities)

#remove duplicates in a list
print('la nueva lista',a_newest_list)
a_set=set(a_newest_list)
a_newest_list_without_duplicates=list(a_set)
print('la nueva lista sin duplicados',a_newest_list_without_duplicates)

#Todo de un golpe anidando las llamadas set en list
print('Se puede hacer todo en una sola sentencia de python list(set(a_newest_list))',list(set(a_newest_list)))

#length de listas len(list)
print('la longitud de la lista a_newest_list es',len(a_newest_list), 'mientras que la longitud de la lista a_newest_list_without_duplicates',len(a_newest_list_without_duplicates))

#Contando ocurrencias en una lista con .count
print('el numero de veces que aparece "pedro" en la lista llamada "a_newest_list" es:', a_newest_list.count('pedro'))

#Check if a item is in the list
if 'pedro' in a_newest_list:
    print('pedro esta incluido en la lista llamada "a_newes_list"')

#Find the index -enconctrar el index de un elemento de la lista
print('el indice del primer elemento de la lista llamada "a_newest_list" que contiene "pedro" es:',a_newest_list.index('pedro'))

#convert list to string con str(list)
print('la string de la lista "a_nested_list" es', str(a_nested_list))

#sorting -ordenar listas en python mediante method .sort o mediante la funcion sorted()

# a_list_to_sort =[0,5,'A',True,'a','z','#',10,'Z'] # --->No chuta no  compara instancias de str e int

print('************* sorting lists with IN-PLACE method .sort()*****************')

# In-place list sort in ascending order

a_list_to_sort =[0,5,True,10,False,1] # chuta False=0, True=1

print('la lista sin ordenar es', a_list_to_sort)
a_list_to_sort.sort() # In-place list sort in ascending order
print('y la lista ordenada es',a_list_to_sort)
a_list_to_sort.sort(reverse=True) # In-place list sort in descending order
print('y la lista ordenada descencente es',a_list_to_sort)


print('************* sorting lists with sorted(list) BUILT_IN function*****************')


a_unsorted_list=['%','a','Z','d','_','H']
print('los elementos de la lista ordenados ascencentemente son', sorted(a_unsorted_list)) # for more check https://en.wikipedia.org/wiki/UTF-8
print('la lista permanece desordenada',a_unsorted_list) # no es IN-PLACE
print('los elementos de la lista ordenados descencentemente son', sorted(a_unsorted_list,reverse=True)) # for more check https://en.wikipedia.org/wiki/UTF-8
print('la lista permanece desordenada',a_unsorted_list) # no es IN-PLACE

print('OPERACIONES CON LISTAS -PARTE 2')
print('\n')

print('XXXXXXXXXXXXXXXXXXX---SLICING-LIST,TUPLAS,STRINGS--my_list[start:stop:step]XXXXXXXXXXXXXXXXXXX')

a_alpha_list=['A','B','C','D','E','F','G','H','I','J','K']
print('una rebanada de los elementos de la lista conteniendo el elementos desde la C(index=2) hasta la I(index=-2), en pasos de a 2',a_alpha_list[2:-2:2])
print('La lista no se modifica, permanece igual', a_alpha_list)
print('otra rebanada hacia atras y de uno en uno',a_alpha_list[-2:-7:-1])
a_alpha_sublist=a_alpha_list[::-3]
print('la sublista de elementos en pasos de a 3', a_alpha_sublist)

print('XXXXXXXXXXXXXXXXXXX---REVERSE LIST in_place . reverse() and others XXXXXXXXXXXXXXXXXXX')

# In-place reverse
a_alpha_list.reverse()
print('Using list reverse:', a_alpha_list)
# Let's revert that...
a_alpha_list.reverse()

# Create a new, reversed list with slices descendant
a_alpha_list_reversed= a_alpha_list[::-1]
print('Reversed 2nd list: ', a_alpha_list_reversed)

# Or use a reversed iterator
rev = reversed(a_alpha_list)
print('Reversed iterator: ', list(rev))


print()
print('**************-------------**************')
print()

# Ejemplos de print()
print(a_boolean_true,a_string,a_integer_number, a_float_number) #separados por ' ' (espacio)
print(1)
print('Some text')
print('A tab:\t and some text')
print() #new line
print('This is my age:', 39)

# Ejemplo de if -else
door_is_locked = True
if door_is_locked:
    print("Mum, open the door!")
else:
    print("Let's go inside")


# Ejemplos de comparaciones y operador logico

if (a_integer_number > a_float_number) and a_boolean_true:
    print(f'el mayor numero es {a_integer_number} porque la operacion logica con -and- tb se cumple')


if (a_integer_number < a_float_number) or a_boolean_false:
    print(f'el mayor numero es {a_integer_number} porque la operacion logica con -and- tb se cumple')
else:
    print(f'el menor numero {a_float_number} porque la operacion logica con -or- tb retorna falso')

# Otros comparadores posibles
verdadomentira = "1"<"a"
print(f'Se puede comparar string de caracteres por ejemplo,"1"<"a" es true -->{verdadomentira}')
verdadomentira = "M"<"m"
print(f'Se puede comparar string de caracteres por ejemplo,"M"<"m" es true -->{verdadomentira}')
verdadomentira = "ana"<"anamaria"
print(f'Se puede comparar string de caracteres por ejemplo,"ana"<"anamaria" es true -->{verdadomentira}')
verdadomentira = "manuel"<"anamaria"
print(f'Se puede comparar string de caracteres por ejemplo,"manuel"<"anamaria" es false -->{verdadomentira}')
verdadomentira = "Manuel"<"anamaria"
print(f'Se puede comparar string de caracteres por ejemplo,"Manuel"<"anamaria" es true -->{verdadomentira}')

#Ejemplos de For y While (loops - bucles) e Iterables (string es un iterable por letters)

print('FOR FOR FOR FOR')

for letter in "hello 2023!":
    print(letter)

my_list = ['Esperamos', 'que', 'el año', 2023, 'sea un buen año desde el dia', 1, 'al 31 de diciembre'] #lista con [] y puede tener diferentes tipos, incluso listas de listas
for item in my_list:
    print(item)

print('WHILE WHILE WHILE WHILE')

i = 1
while i <= 5:
    print(my_list[i])
    i = i + 1

#Appple Street - Infinite loop o inicio (3)
verdadomentira = True
i=1
i_max= 10
while verdadomentira:
    print(f'Infinite loop {i}')
    i = i+1
    if i>i_max:
        verdadomentira=False

#Iterables e Iterators

print('ITERABLES')
my_iterable = range (2, 7, 2) # rango del 2 al 8 en pasos de a 2, range (7) del 0 al 7, range (3,6) del 3 al 6 en saltos de a 1
my_iterator = my_iterable.__iter__()  # objeto range es iterable
print(f'el primer iterador es {my_iterator.__next__()}') #el primer iterador es 2
print(f'el segundo iterador es {my_iterator.__next__()}')
print(f'el tercer iterador es {my_iterator.__next__()}')
# print(f'el cuarto iterador es {my_iterator.__next__()}')

#Funciones

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





