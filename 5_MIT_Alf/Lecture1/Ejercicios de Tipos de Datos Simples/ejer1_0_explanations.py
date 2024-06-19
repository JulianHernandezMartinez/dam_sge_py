# Slides Lecture 2 code 
"""
hi = "hello there"
name = "Julian"
greet = hi + name
greeting = hi + " " + name
silly = hi + " " + name * 3
print(greeting)
print(silly)


# types and type converter / casting
x=1
print(type(x))
x_str = str(x)
print(type(x_str))
print("my fav number is",x,".","x=",x)
print("my fav num is " + x_str+ ". " + "x = " + x_str)


text = input("Type anything... ")
print (text*5)
number = int(input("Enter an integer..."))
print(number*5)
float = float(input("Enter an float..."))
print(float*5)


derive = True
drink = False
both = drink and derive
print(both) 

YassinAge= 19
JulianAge = 57
print(JulianAge > YassinAge)

if YassinAge < 18:
    print("Hola Amigos")
    print("Yassin no puede votar")
else:
    print("Yassin ya puede votar")
    print("Yassin puede entrar en prision")

if JulianAge < 67:
    print("Julian no se puede jubilar")
    print("Pero Julian esta bien de salud")



a = 0
if (a < 0):
    print('a es un número negativo')
elif (a == 0):
    print('a es 0')
elif (a <= 100):
    print('a está entre 1 y 100')
else:
    print('a es mayor que 100') 

"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks!")