# interes compuesto
# https://www.finect.com/usuario/santiagobaron/articulos/que-interes-compuesto

quantity = float(input("Quantity (€)? :"))
rate = float(input("% Rate per year? :"))
years = float(input("Years invested ? :"))
result = round((quantity*((1+rate/100))**years),2)
print(f'after {years} years of {quantity}€ invested with a {rate} % rate you will receice back {(result)}€')




