"""
Escribir un programa que pregunte al usuario por 
el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le 
corresponde.
"""

horas = float(input('cuantas horas has trabajado?'))
coste = float(input('que coste en € por hora tienes?'))
paga = horas*coste
print(f'te corresponde una paga de {paga} €')