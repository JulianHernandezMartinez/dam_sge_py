#tipos y estructuras de datos (tuplas, ranges, list, sets, dictionaries...)
print('\nConstructores de  string-->Set?\n')

print('Este playground pretende mostrar')
print('la potencia a la hora de ir desde')
print('un string a un set o lista directamente...\n')

print('... o no\n')

# desde string a set --OK
an_string="abcde_%@123412ab"
print(an_string)
a_set=set(an_string)
print(a_set)

# y viceversa desde set a string?
an_string=str(a_set)
print(an_string)

print(f'\nla unica manera de distinguir si en la consola estamos \nimprimieno un string o un set es mediante \nla lectura del tipado\n')

print(f'"a_set" es del tipo {type(a_set)}')
print(f'"an_string" es del tipo {type(an_string)}')

a_new_string="ab123ab" # punto de partida
a_tupla=tuple(a_new_string) # string->tupla
a_list=list(a_new_string) #string->lista   
the_same_list=list(a_tupla) #string->tupla->lista
print(a_list == the_same_list) #True
print(a_list,the_same_list)

a_new_set=set(a_new_string)# string->set
the_same_new_set=set(the_same_list)#string->tupla->list->set
print(a_new_set==the_same_new_set)#True

an_string="abc@12ab"
a_list=list(an_string)
a_tupla=tuple(a_list)
a_list=list(a_tupla)
a_set=set(a_list)
print(f"SUMARIO de representacion string '', tupla(), lista[], set{{}} con len(x)")
print(f'an_string  {an_string} y su long. es .{len(an_string)}')
print(f'a_tupla () {a_tupla} y su long. es {len(a_tupla)}')
print(f'a_list  [] {a_list} y su long. es {len(a_list)}')
print(f"a_set   {{}} {a_set} y su long. es {len(a_set)}")
