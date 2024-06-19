age = int(input("age? :"))
if age < 4:
    print("free entrance, free ticket for younger than 4 years old")
elif age < 18:
    print("entry ticket for age among 4 and 18 is 5€")
else:
    print("entry ticket for older than 18 is 10€")
