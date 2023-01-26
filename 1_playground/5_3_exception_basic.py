"""
Breve extracto de clase de exceptiones de Python

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError

      """

# una excepcion es una condicion"excepcional"
# que se alcanza# durante la ejecucion de
# un programa.
# 
# ES una señal de que algo inesperado ha sucedido

try:
    print(10/0)
except ZeroDivisionError:
    print('No se puede dividir por cero')

try:
    # Open file in read-only mode
    with open("53nothere.txt", 'w') as f:
        f.write("Hello World!")
except IOError as e:
    print("An error occurred:", e) #BEST PRACTICES esa e es ORO

# que pasa si creamos el fichero y lo abrimos 
# con Write mode

finally:
    print("Closing the file now")
    f.close()


