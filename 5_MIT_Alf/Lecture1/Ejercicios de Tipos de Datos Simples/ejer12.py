breadprice = 3.49
nofreshdiscount = 0.60 # 60% discount when no fresh
breads = int(input("Breads? :"))
print(f'The normal bread price is {breadprice}€')
print(f'The discount for no fresh bread is {round(breadprice*nofreshdiscount,2)}€')
print(f'The final total cost of {breads} no fresh breads is {round(breads*(round(breadprice*nofreshdiscount,2)),2)}€')

