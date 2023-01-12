a = "Pere"
b = "Pol"

# las longitudes son iguales: False
print(len(a) == len(b))
print(not(len(a) != len(b)))
# todas tienen longitud 3: False
print(len(a) == 3 and len(b) == 3)
print((len(a) == 3) and (len(b) == 3))

# alguna longitud es menor de 4: True
print(len(a) < 4 or len(b) < 4)
# alguna termina con l: True
print(a[-1] == "l" or b[-1] == "l")
# todas comienzan por P: True
print(a[0] == "P" and b[0] == "P")
# alguna no contiene la r: True
print(a.find("r") == -1 or b.find("r") == -1)
# la longitud de a es mayor que la de b: True
print(len(a) > len(b))
# la longitud de a NO es mayor que la de b: False
print(not(len(a) > len(b)))
# la longitud de a está entre 3 y 4 y la de b no es menor que la de a: False
print(len(a) >= 3 and len(a) <= 4 and not(len(b) < len(a)))
print(len(a) >= 3 and len(a) <= 4 and len(b) >= len(a))
