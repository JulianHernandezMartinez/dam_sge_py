"""ENUNCIADO

 haz un programa que pregunte dos 
 palabras y que saque las 

# asdf | asdf ==> exactamente iguales
# asdf | ASDF ==> iguales ignorando mayusculas-mnusculas
# asdf | a s d f ==> iguales ignorando espacios
# asdf | A S D F ==> igualess ignorando mayusculas y espacios

"""





#SOLUCION

str1 = input("1? ")
str2 = input("2? ")

str1m = str1.upper()
str2m = str2.upper()
str1s = str1.replace(" ", "")
str2s = str2.replace(" ", "")
str1sm = str1.upper().replace(" ", "")
str2sm = str2.upper().replace(" ", "")

if str1 == str2:
    print("exactamente iguales")
else: 
    if str1m == str2m:
        print("iguales ignorando 'case sensitive'")        
    elif str1s == str2s:
        print("iguales ignorando espacios")        
    elif str1sm == str2sm:
        print("iguals ignorando case y espacios")        
    else:
        print("diferentes")

# asdf | asdf ==> exactament iguals
# asdf | ASDF ==> iguals ignorant case
# asdf | a s d f ==> iguals ignorant espais
# asdf | A S D F ==> iguals ignorant case i espais




