passwordtosave = input("password? :")
passwordtocheck = input("repeat password")

if passwordtosave.lower() == passwordtocheck.lower():
    print("passwords matchs")
else:
    print("passwords are not equals")
