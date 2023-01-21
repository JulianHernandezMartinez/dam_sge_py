
print('Sentencias o formas basica, IF.. Else, While, For.. print & input')


a_string = "hola caracola" #cadena de caracteres

a_integer_number = 123
a_float_number = 12.3456
a_boolean_true = True
a_boolean_false = False
a_new_boolean_true = True
a_new_boolean_false = False
verdadomentira = True

# sentencia para asignar una entrada 
# de datos desde la entrada por defecto, 
# la consola, y convertirla en un numero
# entero int(x)  x=input()

# input example - total_segundos = int(input("segundos? "))

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
print(f'for loop finished!\n')

my_list = ['Esperamos', 'que', 'el año', 2023, 'sea un buen año desde el dia', 1, 'al 31 de diciembre'] #lista con [] y puede tener diferentes tipos, incluso listas de listas
for item in my_list:
    print(item)
print(f'new for loop finished!\n')

print('WHILE WHILE WHILE WHILE\n')

i = 1
while i <= 5:
    print(my_list[i])
    i = i + 1
print(f'while loop finished!\n')

#Appple Street - Infinite loop o inicio (3)
verdadomentira = True
i=1
i_max= 6
while verdadomentira:
    print(f'loop {i}')
    i = i+1
    if i>i_max:
        verdadomentira=False
print(f'while loop finished!')


