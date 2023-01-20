# string como array, y sub-arrays


v1 = "abcde"
v2 = v1[1:3]
print("de 1 a 3", v2)
v3 = v1[:1] + v1[3:]
print("sin del 1 al 3", v3)


posicion = 3
cadena = "ABCDEFG"
subcadena = cadena[posicion]
print(subcadena)

cadena = "alfa,beta,gamma"
a,b,g = cadena.split(",")
print(f"separado en {a}, {b} y {g}")

