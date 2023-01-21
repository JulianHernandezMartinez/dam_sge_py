num = int(input("número? "))
if num == 0:
    print("es cero")
else:
    if num % 2 == 0:
        print("es par!")
    else:
        print("es impar!") 

num = int(input("número? "))
if num == 0:
    print("es cero")
elif num < 0:
    print("es negativo!")
elif num % 2 == 0:
    print("es par!")
else:
    print("es impar!")


edat = int(input("edad? "))
if edat <= 3:
    print("bebé")
elif edat <= 12:
    print("niño")
elif edat < 18:
    print("adolescente")
else:
    print("mayor de edad")

