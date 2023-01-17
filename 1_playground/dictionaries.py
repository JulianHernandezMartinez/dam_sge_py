agenda_telefonica ={'ana':'600123456', 'leo':'610123456','paz':'666654321', 'emergencias':'112', 'ayuntamiento':'010'}
print(agenda_telefonica)
diccionario_runners ={} #Diccionario vacio para incluir los corredores de una carrera
print(diccionario_runners)

#acceder a un elamento del dict con dict['key'] en nuestro caso agenda_telefonica['ana]
print('el telefono de ana es el', agenda_telefonica['ana']) 
# peta, solo acepta la >key y la key siempre es el primer elemento print('la persona que tiene el telefoo 600123456 se llama', agenda_telefonica['600123456'])
print('el telefono de paz es el',agenda_telefonica.get('paz'))

#get retorna "None" si la key no existe

print('el telefono de roberto es el',agenda_telefonica.get('roberto'))

# sin embargo el acceso directo dict['key'], con un key inexistente resulta en una excepcion de keyError
# print('el telefono de federica es el', agenda_telefonica['federica']) 

#borrar entrada en diccionario

del(agenda_telefonica['paz'])
print(agenda_telefonica)

#Modificar valor (overwrites)
agenda_telefonica['ana']='700123456'
print(agenda_telefonica)

#pueden incluir como valores enteros, strings, y tb tuplas, listas y otros diccionarios

a = { 'sub_dict': { 'b': True },'mylist': [100, 200, 300] }

print("""el elemento de index=2 de la lista con la key 'mylist' es""",a['mylist'][2])
print("""y el valor asociado a la key 'b' del diccionario con key 'sub_dict' es""",a['sub_dict']['b'])