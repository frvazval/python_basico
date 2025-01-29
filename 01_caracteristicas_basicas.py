"""
CARACTERISTICAS BÁSICAS DE PYTHON
"""
# =============================================================================================================
# VARIABLES
# Una variable es un espacio en memoria para guardar datos
# por tanto, es un contenedor

# Para crear una variable...
# identificador = valor

# Hay reglas para llamar a los identificadores = nombre de la variable
# No se puede hacer:
#       1variable (empezar por un número, después si lo puede llevar)
#       $variable (ni empezar ni contener simbolos especiales)
# De estos errores nos avisará VSC

# No debemos hacer (no son exactamente errorres):
#       Contener caracteres fuera del idioma inglés, como Ñ, Ç, tildes, á, ö, etc
#       Empezar por guión bajo (reservado para determinadas situaciones)
#       Utilizar palabras reservadas del sistema (True, False, Etc...)

# Qué debemos hacer:
#       Nombrar a nuestras variables con palabras descriptivas
#       Podemos usar más de una palabra separadas por un guioón bajo (directiva PEP-8)
#       Intentar que las líneas de código no sean muy largas

"""
Las variables tienen tipo
        -- números -> enteros (int), decimales (float), complejos
        -- texto -> strings
        -- booleanos -> True / False

        En Python, por defecto NO existen las constantes

        PI = 3.1416  -> se escribe en mayusculas para identificarla en el codigo como una constante

        PYTHON ES DE TIPO DINÁMICO

        número = 1 # entero
        número = "uno" string

        PYTHON ES DE TIPADO FUERTE

        suma = numero + 2 # Error -> no se pueden sumar números y texto
        concatenación = numero + str(2)
        suma_numerica = int("1") + 2

"""
