juli_ciclista=True
manu_ciclista=False
ana_ciclista=False
eva_ciclista=True

print('----Operadores logicos, or, and, not----')


if  juli_ciclista or manu_ciclista:
   print('al menos uno de los dos es ciclista')
else: 
   print('ninguno de los dos es ciclista')

if ana_ciclista or manu_ciclista:
   print('ninguno de los dos es ciclista')
else: 
   print('al menos uno o los dos son ciclistas')

if eva_ciclista and juli_ciclista:
   print('los dos son ciclistas')
else: 
   print('los dos no son ciclistas')

if eva_ciclista and ana_ciclista:
   print('las dos son ciclistas')
else: 
   print('las dos no son ciclistas')
   
a_integer_number = 123
a_float_number = 12.3456
a_boolean_true = True
a_boolean_false = False
a_new_boolean_true = True
a_new_boolean_false = False
verdadomentira = True

verdadomentira = a_float_number<a_integer_number
print(verdadomentira) #True
verdadomentira =a_new_boolean_false==a_boolean_false
print(verdadomentira) #True
verdadomentira = a_float_number<=a_integer_number
print(verdadomentira) #True

verdadomentira = a_float_number > a_integer_number
print(verdadomentira) #False
verdadomentira =not a_new_boolean_false==a_boolean_false
print(verdadomentira) #False
verdadomentira = a_float_number>=a_integer_number
print(verdadomentira) #False