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

variable = "otra cosa"

def prueba_variables():
    variable = "Soy una prueba" # solo es accesible desde dentro de la variable

print(variable)


# valor por defecto

def mostrar_datos_alumno(nombre, apellido, becado = False):
    if becado:
        becado = "Sí"
    else:
        becado = "No"
        
    return f"el alumno {nombre} {apellido} tiene beca? --> {becado}"

alumno_1 = mostrar_datos_alumno("Anna", "Garcia")
print(alumno_1)
alumno_2 = mostrar_datos_alumno("Joan", "Pou", True)
print(alumno_2)

