"""
FUNCIONES
"""
# declaración de la función
def sumar():
    print(1 + 2)

# invocación de la función
sumar()

# declaración con devolución de valor
def sumar():
    return 1 + 2

print(sumar())

# declaración pasandole valores
# lo que hay dentro del parentesis son los PARAMETROS
def sumar(num1, num2):
    return num1 + num2

# en la invocación lo que esta dentro de los parentesis son los ARGUMENTOS
print(sumar(3,7)) 
print(sumar(3.5, 7.2))
print(sumar("Hola ","y adios"))

resultado = sumar(3,2)
print(resultado)

