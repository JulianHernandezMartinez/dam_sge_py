weight = float(input("your weigth please in kg : "))
height = float(input("your heigth please in meters : "))
bmi = round(weight/(height)**2,2)
print (f'Your bmi is {bmi}.')

if (bmi < 16):
    print('Underweight (Severe thinness)')
elif (bmi < 16.9):
    print('Underweight (Moderate thinness)')
elif (bmi < 18.4):
    print('Underweight (Mild thinness)')
elif (bmi < 24.9):
    print('Normal range')
elif (bmi < 29.9):
    print('Overweight (Pre-obese)')
elif (bmi < 34.9):
    print('Obese (Class I)')
elif (bmi < 39.9):
    print('Obese (Class II)')
else:
    print('Obese (Class III)')


