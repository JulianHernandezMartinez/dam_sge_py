divident = int(input("give me divident : "))
divider = int(input("give me divider : "))
remainder = divident%divider
quotient = int(divident/divider) # truncates float values
print(f'{divident} divided by {divider} gives a quotient of {quotient} and a remainder of {remainder}')


# Another choices / options
import math
quotient = math.floor(divident/divider)
print(f'{divident} divided by {divider} gives a quotient of {quotient} and a remainder of {remainder}')
