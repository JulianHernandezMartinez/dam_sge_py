# Crea un programa que lee 3 números y los muestra ordenados de mayor a menor.

p1 = int(input("1? "))
p2 = int(input("2? "))
p3 = int(input("3? "))

if p1 >= p2 and p1 >= p3:    
    if p2 >= p3:
        o1 = p1; o2 = p2; o3 = p3
    else:
        o1 = p1; o2 = p3; o3 = p2
elif p2 >= p1 and p2 >= p3:
    if p1 >= p3:
        o1 = p2; o2 = p1; o3 = p3
    else:
        o1 = p2; o2 = p3; o3 = p1
elif p3 >= p1 and p3 >= p1:
    if p1 >= p2:
        o1 = p3; o2 = p1; o3 = p2
    else:
        o1 = p3; o2 = p2; o3 = p1

print(f"el orden de mayor a menor es {o1}, {o2}, {o3}")

