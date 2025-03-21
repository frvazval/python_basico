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

    return f"el alumno {nombre} {apellido} tiene beca? --> {becado}" # es la ultima instruccion, porque lo que va detras ya no lo ejecuta

alumno_1 = mostrar_datos_alumno("Anna", "Garcia")
print(alumno_1)
alumno_2 = mostrar_datos_alumno("Joan", "Pou", True)
print(alumno_2)

# Queremos hacer una función que sume los numeros que le pasemos por argumento, (cualquier cantidad)
# ejemplos
# ========
# sumar(1,2)
# sumar(3,4,5)
# sumar(6,4,5,3)

def sumar(*argv): # argumentos variados, se puede llamar de otra forma, pero se suele llamar argv
    print(argv)
    print(type(argv)) # argv es una tupla

sumar(1,2)
sumar(3,4,5)
sumar(3,4,5,3)

# El return puede devolver más de un valor
# Opcionalmente se le puede indicar que es un string y que devuelve un string
def separarNombre(apellido_nombre : str) -> str:
    # Para que muestre la ayuda al poner el cursor encima
    """
    Devolverá de forma separada el nombre y el apellido

    @ Params\n
    str -> "Apellido, Nombre"

    @ Return\n
    str -> Nombre, str -> Apellido\n
    """
    palabras = apellido_nombre.split(",")
    apellido = palabras[0].strip()
    nombre = palabras[1].strip()
    return nombre, apellido

nombre, apellido = separarNombre("Vázquez, Francisco")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")

# Muestra la ayuda de la función
help(separarNombre)
print(separarNombre.__doc__)



