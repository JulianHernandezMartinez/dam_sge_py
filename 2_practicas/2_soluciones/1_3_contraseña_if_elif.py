
# pregunta una contraseñaa
# si es "demasiado corta" o "demasiado larga", lo decimos y finalizamos
# si no, solicita repetir la contraseña
# si son iguales di "iguales", si no lo son, di "diferentes"

# asdf | asdf ==> iguales
# asdf | qwer ==> diferentes
# asdfasdfa ==> demasiado larga
# as ==> dedasiado corta
# 
# Escribe tu solucion aqui: 
#
# SOLUCION
#


str = input("contraseña? ")
if len(str) < 3:
  print("demasiado corta")
elif len(str) > 8:
  print("demasiado larga")
else:
  str2 = input("repetir? ")
  if str == str2:
    print("iguales")
  else:
    print("diferentes")





# pregunta una contraseñaa
# si es "demasiado corta" o "demasiado larga", lo decimos y finalizamos
# si no, solicita repetir la contraseña
# si son iguales di "iguales", si no lo son, di "diferentes"

# asdf | asdf ==> iguales
# asdf | qwer ==> diferentes
# asdfasdfa ==> demasiado larga
# as ==> dedasiado corta
