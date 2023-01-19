
# pregunta una palabra (por ejemplo: avión) 
#y escribe por pantalla:
# avión tiene 5 letras
# de tres formas:
# 1) print con un parámetro y concatenación de strings
# 2) print con varios parámetros separados por comas
# 3) f print funcion

palabra = input("palabra? ")
print(palabra + " tiene " + str(len(palabra)) + " letras") #concatenando
print(palabra, len(palabra), "letras")  #Varios parametros separados por comas
print(f"{palabra} tiene {len(palabra)} letras") # funcion f'