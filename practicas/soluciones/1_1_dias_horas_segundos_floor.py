
SEGUNDOS_1_DIA = 60*60*24
SEGUNDOS_1_HORA = 60*60
SEGUNDOS_1_MINUTO = 60

total_segundos = int(input("segundos? "))

dias = total_segundos // SEGUNDOS_1_DIA
resto1 = total_segundos % SEGUNDOS_1_DIA

horas = resto1 // SEGUNDOS_1_HORA
resto2 = resto1 % SEGUNDOS_1_HORA

minutos = resto2 // SEGUNDOS_1_MINUTO
resto3 = resto2 % SEGUNDOS_1_MINUTO

print(f"{dias} dias, {horas} horas, {minutos} minutos y {resto3} segundos")




# Solicitamos un numero de segundos con "Segundos?"
# calculamos y decimos los dias, horas y segundos
# ejemplo 120000 segundos -->1 dias, 9 horas, 20 minutos y 0 segundos
# funcion de componer "srings" f'
