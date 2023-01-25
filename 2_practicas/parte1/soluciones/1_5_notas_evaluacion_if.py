
"""Crea un programa que solicite 
al usuario la nota de las 3 examenes 
del módulo de programación. Después, 
debe calcular la nota final del módulo, 
teniendo en cuenta lo siguiente: el 
primer examen vale el 20%, 
el segundo vale el 30% y el tercer 
vale el 50%. 

Después de calcular la nota final, 
debe mostrar al usuario si está aprobado 
o no. 

En caso de que esté aprobado, además 
debe mostrar la nota final. 

En caso de que esté suspendido, la nota 
final no se mostrará.

"""

uf1 = float(input("nota de primer examen (0-10)? "))
uf2 = float(input("nota del segundo examen (0-10)? "))
uf3 = float(input("nota del tercer examen (0-10)? "))

nota = uf1*20/100 + uf2*30/100 + uf3*50/100
aprovado = nota >= 5

if aprovado:
    print(f"Tu nota es {nota}")
else:
    print("has suspendido")