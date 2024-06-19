# interes compuesto
# https://www.finect.com/usuario/santiagobaron/articulos/que-interes-compuesto

quantity = float(input("Quantity (€)? :")) #Quantity to invest
rate = 4.0 # Interes rate
years = 1.0 # years invested
result = round((quantity*((1+rate/100))**years),2)
print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')
years = 2.0
result = round((quantity*((1+rate/100))**years),2)
print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')
years = 3.0
result = round((quantity*((1+rate/100))**years),2)
print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')

#With a lovely  for...

quantity = float(input("Quantity Second Time (€)? :"))
for years in range(1,4):
    result = round((quantity*((1+rate/100))**years),2)
    print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')

#With a lovely  For...
#and a lovely Function
# The function
quantity = float(input("Quantity Third Time (€)? :"))
def composerate(quantity,rate,years):
    result = round((quantity*((1+rate/100))**years),2)
    print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')

#The for
for years in range(1,4):
    composerate(quantity,rate,years)



