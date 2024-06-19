price = input("Enter price with 2 decimals :")
print (f'the price is {price[:price.find(".")]}€ and {price[price.find(".")+1:]} cents')

print (f'the price is {round(float(price),2)}')
