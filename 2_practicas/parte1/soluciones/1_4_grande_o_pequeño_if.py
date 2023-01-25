
""" Crea un programa que pida 
3 números y que diga cual es el 
mas grande y cual es el mas pequeño.








SOLUCION """

num1 = int(input("número 1? "))
num2 = int(input("número 2? "))
num3 = int(input("número 3? "))

if num1 >= num2 and num1 >= num3:
    grande = num1
elif num2 >= num1 and num2 >= num3:
    grande = num2
else:
    grande = num3

if num1 <= num2 and num1 <= num3:
    pequeño = num1
elif num2 <= num1 and num2 <= num3:
    pequeño = num2
else:
    pequeño = num3

print(f"el mas pequeño es el {pequeño}, y el mas grande es {grande}")