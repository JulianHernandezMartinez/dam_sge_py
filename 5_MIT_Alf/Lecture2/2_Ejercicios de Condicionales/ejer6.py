sex = input("Sex? (male/female) :").lower()
name = input("Name ? :").lower()
if ((sex == "female") & (name < "n")) | ((sex != "female") & (name > "m")) :
    print ("belong to A group")
else:
    print("belong to B group") 