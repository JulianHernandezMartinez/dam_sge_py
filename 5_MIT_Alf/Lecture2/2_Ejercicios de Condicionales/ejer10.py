veggie = input("Veggie? (Y/N):") == "Y"
# print(veggie)
if veggie:
    ingredient = input("Choose either Peper or Tofu: ")
    print (f'Veggie Pizza with Mozarella, Tomatoe and {ingredient}')
else:
    ingredient = input("Choose either Peperoni, Ham or Salmon: ")
    print (f'No Veggie Pizza with Mozarella, Tomatoe and {ingredient}')
