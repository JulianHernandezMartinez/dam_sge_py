cadena = "Hola, como vas?"
p = cadena.find("com")
longitud = len(cadena)
print(p, longitud)

cadena2 = cadena.replace("Hola", "Hello")
print(cadena2)
print("Tachan"*2)

a = "CADENA en minúsculas"
la = a.lower()
print(la)
print(a[7:9], a[-5:], a[-4], a[10:-1], a[::4])
print("al revés", a[::-1])

print(a.capitalize())
print(a.title())
