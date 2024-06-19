income = int(input("anual income? :"))
if income > 0:
    if income < 1000:
        print("tax rate = 5%")
    elif income < 2000:
        print("tax rate = 15%")
    elif income < 35000:
        print("tax rate = 25%")
    elif income < 60000:
        print("tax rate = 30%")
    else:
        print("tax rate = 45%")    
else:
    print("please enter a positive value")