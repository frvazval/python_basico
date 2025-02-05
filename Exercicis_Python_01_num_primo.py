"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""
import os # importa libreria os
        
os.system("cls") # Limpia la pantalla

es_primo = True # En el caso de que no sea primo tendra el valor False

for intento in range(3): # Pide el número 3 veces
    # Gestiono las excepciones con try / except (ValueError, por si no introduce un entero válido)
    try:     
        # Muestra el número de intento actual
        print(f"Número de intento -> {intento + 1} (tienes 3 intentos)")

        # Pide el número entero 
        num = int(input("Introduce un número entero: "))

        # Compruebo si el número es primo o no lo es 
        for n in range(2, num):
            if num % n == 0:
                es_primo = False # No es primo
                break             
        
        # Muestro el mensaje correspondiente dependiendo del valor de la variable es_primo
        if es_primo == True:
            print(f"El número {num} es primo")
            break
        else:
            print(f"El número {num} no es primo")
            break                       

    except ValueError: # Si el valor introducido no es un número entero
        print("Has de introducir un número entero")
else:
    print("No has podido introducir un número entero en tres oportunidades")
    print("Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.")




    