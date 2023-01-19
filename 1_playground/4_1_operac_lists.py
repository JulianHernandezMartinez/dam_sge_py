print('OPERACIONES CON LISTAS -PARTE1\n')
print('Create, Sort, Append, Remove, And More)\n')

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


