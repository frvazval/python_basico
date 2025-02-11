"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

try:

    print("Conversor de segundos")
    print("=====================")

    # pido la cantidad de segundos

    segundos = int(input("Cantidad de segundos: "))

    if segundos < 60:
        print(f"{segundos} segundos son menos de 1 minuto")
    elif segundos >= 60:
        pass

except ValueError: # Error de que ha introducido letras en lugar de números
    print("Hay que introducir un número valido")