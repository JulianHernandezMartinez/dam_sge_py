weight = float(input("your weigth please in kg : "))
height = float(input("your heigth please in meters : "))
bmi = round(weight/(height)**2,2)
print (f'Your bmi is {bmi}.')
idealbmi = 23
if (bmi < 16):
    print('Underweight (Severe thinness)')
    bmistate = "underweight"
elif (bmi < 16.9):
    print('Underweight (Moderate thinness)')
    bmistate = "underweight"
elif (bmi < 18.4):
    print('Underweight (Mild thinness)')
    bmistate = "underweight"
elif (bmi < 24.9):
    print('Normal range')
elif (bmi < 29.9):
    print('Overweight (Pre-obese)')
    bmistate = "overweight"
elif (bmi < 34.9):
    print('Obese (Class I)')
    bmistate = "overweight"
elif (bmi < 39.9):
    print('Obese (Class II)')
    bmistate = "overweight"
else:
    print('Obese (Class III)')
    bmistate = "overweight"

# bmi = weight/(height)**2
# idealbmi = 23
# idealweigth = 23 * (height**2)
idealweigth = round(23 * (height**2),2)
print(f'Your ideal weigth is {idealweigth} kg.')

if idealweigth < weight:
    print(f'you should reduce your weigth in {round(weight-idealweigth)} kg')
else:
    print(f'you should increase your weigth in {round(idealweigth-weight)} kg')


