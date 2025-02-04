"""
RESUMEN SIMPLIFICADO DE LO ESENCIAL
"""

# SINTAXIS BASICA
# Python indenta lo que pertenece al mismo bloque dentro de una condición
# Python diferencia mayusculas de minusculas

# VARIABLES
# Es un contenedor de un elemento
# es un identificador para ubicar un elemento guardado en la memoria

int = 1
float = 1.0
string = "hola"
boolean = True  # o False

# Aunque sean vacíos hay que indicar valores

string =""
int = 0
lista = []

# OPERADORES
# -- de tipo matématico :
# + (suma), - (resta). etc...
# el signo + permite concatinar strings

saludo = "buenas" + " " + "tardes" # el resultado es : buenas tardes
repeticion = "hola" * 3 # El resultado seria holaholahola

# -- de comparación
# == (igual), != (diferente), > (mayor), >= (mayor o igual), < (menor), <= (menor o igual)
# -- siempre devuelven un valor booleano
# -- también se pueden comparar string


# -- de asignación : 
# -- = (asignación), += (suma y asignación). -= (resta y asignación)

int = 5
int = int + 5 # es lo mismo que int += 5
int += 5 # este es un poco más óptimo

num_str = "5"
num_str = int(num_str) # pasa "5" a entero
num = 5
num = str(num) # lo pasa a string "5" , esto se llama casting

# ESTRUCTURAS DE CONTROL
# CONDICIONALES
# if condición -> ejecutara un código si la condición es verdadera
# if condición/ else -> si la condición no se cumple ejecutara el else
# if condición / elif condición
# if condición / elif condición / más elif ........ / else

# match variable:
#   case valor: # si la variable tiene este valor
#       se ejecuta el código siguiente
# case _: # equivale al else o "default"







