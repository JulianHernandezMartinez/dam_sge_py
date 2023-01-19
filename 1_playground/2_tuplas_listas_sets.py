#tipos y estructuras de datos (tuplas, ranges, list, sets, dictionaries...)
print('\nTipos de estructuras de datos\n')

print('strings(array), TUPLAS, LISTAS, SETS, DICCIONARIOS, arrays  \n')
print('tuplas, listas, sets vs arrays')
print('"politipicos" (multiples tipos) vs tipos estrictos\n')

#TUPLAS('A','B', 1, 5, True)
#tuplas(), -->lists[] --> sets{} -->Dictionaries
print('TUPLAS() - como arrays INMUTABLES\n')

#tuplas,arrays inmutables
persona = ('Erika', 38, True)
print(persona) # imprimme la tupla, incluye los ()
# permite asociar variables a elementos de la tupla
nombre, edad, registrada = persona # name, age y registro con elementos en persona
print(nombre, edad) # Erika 38
#sus elementos, caracteres, se pueden referenciar como elementos indexados de un array
print(persona[1], persona[2],'\n') # 38, True

# las tuplas no se pueden modificar 
# (son INMUTABLES), si se desean ampliar,
# es necesario crear una nueva tupla

print('el operador "*" para desempaquetar, "despeinar/desplegar" tuplas...\n')

t =(1,2,3, 'bici', 'coche', 'moto')
t1 = (*t,5,4,3) # '*' desempaqueta la tupla t, podemos crear t1, en base a t, pero no añadir sobre t
print(t1)

print('\nla funcion len() NUEVAMENTE en string, tuplas, etc\n')

print('la longitud de la tupla "t" es:', len(t), '\nla longitud de la tupla "t1" es:', len(t1),'\n')

print('la funcion str(t) convierte la tupla t en un string',str(t),'\n')

a_new_string=str(t) #str() es el constructor de tipos string
print('la funcion str(t) convierte la tupla t en un string',a_new_string,'\n')

print(f'la funcion str(t) convierte la tupla t en un string {a_new_string} \n')

print('LISTAS[]- como arrays MUTABLES \n')

#lists, arrays mutables y pueden tener elementos repetidos, y tipos diferentes
lista = [8,5,6,7,8,9]
l1=[0,]
print(lista)
l=list(t1) #list es un conversor de tupla en lista, conierte la tupla t1 en una lista l
print(l)

print('\n SETS{} - como arrays MUTABLES sin REPETIDOS \n')
# sets, arrays ORDENADOS y mutables, NO pueden tener elementos repetidos, pueden tener diferentes tipos

s={9,7,5}
s1=set(t) #constructor/conversor de un set a partir de X en el caso una tupla
s2=set(l) #constructor de un set a partir de X, en el caso una lista
s3={}
print('a=',s1,'b=',set(t1),'c=', set(lista),'d=', set(l), 'e=',set(l)==set(t1), 'f=',{},'g=',set(l1),'h=', s3)

print('\nRESUMEN un string se puede considerar un array de caracteres')
print('RESUMEN los constructores son conversores de STRING<->TUPLAS<->LIST<->SETs')


# Create with list() function
a_list_from_0_to_9=list(range(10))
a_list_from_1_to_9=list(range(1,10))
a_list_from_2_to_9_in_steps_of_2=list(range(2,10,2))
print(a_list_from_0_to_9)
print(a_list_from_1_to_9)
print(a_list_from_2_to_9_in_steps_of_2)
# YYY hasta aqui la intro de tuplas, listas y sets

print('\n Fin de TUPLAS, LISTAS y SETS\n')
