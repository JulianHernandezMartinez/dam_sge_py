pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)


#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1

# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!

inputdata = input("Introduce un dato: ")
type(inputdata)
outputdata = inputdata
print (outputdata)

numberthree = 3
type(numberthree)

# Soporte Ejercicios
#Operaciones matematicas simples +, - , *, **, %


# Algorithm
# Calculate the square root of a number with succesive aproximations

x = input("Enter the number you want to know the square root: ")
x = int(x)
guess = x/2
print(guess)

while ((((guess*guess)-x) > 0.2) or (((x-guess*guess)) > 0.2)):
    guess = (guess+x/guess)/2
    #guess = (guess+x/guess)
    print(guess)

# interpolation of string and variables 

# print (f'the square root of {x} is {guess}')

name = "Julian"
print(f'Hello {name}')








