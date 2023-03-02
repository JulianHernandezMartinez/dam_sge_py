# GLOBALES
# Añade las variables globales que necesites para tu programa

noms = [] # nombres
nums = [] # numeros

# FUNCIONES
# Añade las funciones que llamarás en la zona MAIN

def mostrarMenu():
    print("\n1: Ver cesta")
    print("2: Añadir ítem")
    print("3: Quitar ítem")
    print("4: Buscar ítem")
    print("5: Vaciar cesta")
    print("6: Salir")


def inputNumero(text, min, max):
    return int(input(f"{text}? "))

def inputText(text):
    return input(f"{text}? ")

def verCesta():
    if len(noms) == 0:
        print("\ncesta vacia")
    else:
        print("\nEn la cesta:")    
        for i in range(len(noms)):
            print(f"  {nums[i]} {noms[i]}")

def buscarItem(nom):
    if nom in noms:
        posicio = noms.index(nom)
        return nums[posicio]
    else:
        return 0

def añadirItem(nom, num):
    if nom in noms:
        posicio = noms.index(nom)
        nums[posicio] = nums[posicio] + num
    else:
        noms.append(nom)
        nums.append(num)

def quitarItem(nom, num):
    if nom in noms:
        posicio = noms.index(nom)
        if num == nums[posicio]:
            del noms[posicio]
            del nums[posicio]
            return True
        elif num < nums[posicio]:
            nums[posicio] = nums[posicio] - num
            return True
        else:
            return False
    else:
        return False

def vaciarItems():
    global noms, nums
    noms = []
    nums = []
    print("cesta vaciada")


# MAIN
# Bucle principal del programa que va llamando las funciones

def main():
    final = False
    while not final:
        mostrarMenu()
        opcion = inputNumero("opción", 1, 6)
        if opcion == 1:
            verCesta()
        elif opcion == 2:
            nom = inputText("nombre")
            num = inputNumero("cantidad", 1, 1000)
            añadirItem(nom, num)
        elif opcion == 3:
            nom = inputText("nombre")
            num = inputNumero("cantidad", 1, 1000)        
            ok = quitarItem(nom, num)
            if not ok:
                print("no se puede borrar")
        elif opcion == 4:
            nom = inputText("nombre")
            num = buscarItem(nom)
            print(f"hay {num}")
        elif opcion == 5:
            vaciarItems()
        elif opcion == 6:
            final = True

if __name__ == "__main__":
  main()
