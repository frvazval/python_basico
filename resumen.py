"""
RESUMEN SIMPLIFICADO DE LO ESENCIAL
"""

# SINTAXIS BÁSICA
# Python "indenta" los bloques de código
# Diferncia mayúsculas de minúsculas


# VARIABLES
# es un contenedor de un elemento
# es un identificador para ubicar un elemento guadado en la memoria

# La variables siempre se declaran antes de ser utilizadas
# también deben ser iniciadas
int = 1
float = 1.0
string = "hola"
boolean = True # False

# aunque sean vacíos hay que indicar valores
string = ""
int = 0
lista = []

# OPERADORES

# -- de tipo matématico :
# + (suma), - (resta), etc
# el signo + permite concatenar strings
saludo = "buenas" + " " + "tardes"
repeticion = "hola" * 3 # "holaholahola"

# -- de comparación :
# == (igual), != (diferente), > (mayor), >= (mayor o igual a ), < (menor), etc
# -- siempre devuelven un valor booleano
# -- También podemos comparar strings
print("Hola" > "hola")

# -- de asignación :
# -- = (asignación), += (suma y asignación), -= (resta y asignación
int = 5
int = int + 5 # es lo mismo que int += 5
int += 5 # este es un poco más óptimo

num_str = "5"
num_int = int(num_str) # casting -> convierte un string a un entero
num_5 = 5 # es un entero
num_5_str = str(num_5) # casting -> convierte un entero a un string

# ESTRUCTURAS DE CONTROL
# CONDICIONALES
# if condicion: -> ejecutará un codigo si la condición es verdadera
# if condicion / else (para todo lo demás)
# if condicion / elif condicion
# if condicion / elif condicion / más elif / else

# match variable:
#   case valor : # si la variable tiene el valor indicado 
#       se ejecuta el código siguiente
# case _ : # equivale al "default"o un else 







