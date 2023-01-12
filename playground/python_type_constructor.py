x = str("Hello World") # str --> usar el constructor asegura que el tipo de esa variable es str
print(""" x = str("Hello World")""")
print(x)
print(type(x))

y="Hola Mundo"  # el interprete hace el autotipado y lo hace bien, le pone un str
print(y)
print(type(y))

z=1j
print(z)
print(type(z))

x = str("Hello World") # str
x = int(20) #int 	
x = float(20.5)#float 	
x = complex(1j)#complex 	
x = list(("apple", "banana", "cherry"))#list 	
x = tuple(("apple", "banana", "cherry"))#tuple 	
x = range(6)#range 	
x = dict(name="John", age=36)#dict 	
x = set(("apple", "banana", "cherry"))#set 	
x = frozenset(("apple", "banana", "cherry"))#frozenset 	
x = bool(5)#bool 	
x = bytes(5)#bytes 	
x = bytearray(5)#bytearray 	
x = memoryview(bytes(5)) #memoryview