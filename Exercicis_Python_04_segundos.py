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
    # variables para guardar los segundos, minutos, horas, dias, etc....
    segundos = 0
    minutos = 0
    horas = 0
    dias = 0

    print("Conversor de segundos")
    print("=====================")

    # pido la cantidad de segundos
    num_seg = int(input("Cantidad de segundos: "))
    mensaje = str(num_seg)
    if num_seg < 60: # Hasta menos de un minuto        
        mensaje += " son menos de 1 minuto"
                
    elif num_seg >= 60 and num_seg < 3600: # de un minuto hasta menos de una hora (60 minutos * 60 son 3600 segundos)
        mensaje += (" son " + str(num_seg // 60) + " minutos") 

        if num_seg % 60 != 0: # Si despues de calcular los minutos aun queda algun segundo 
            mensaje += (" y " + str(num_seg % 60) + " segundos")   

    elif num_seg >= 3600 and num_seg < 86400: # de una hora a menos de un día (en 24 horas hay 86400 segundos, 60 * 60 * 24)
        horas = num_seg // 3600
        mensaje  += (" son " + str(horas) + " horas")  

        if num_seg % 3600 != 0:
            minutos = num_seg % 3600 
            mensaje += (" y " + str(minutos) + " minutos") 

            if minutos % 60 != 0:
                segundos = minutos % 60
                mensaje += (" y " + str(segundos) + " segundos")

    elif num_seg >= 86400 and num_seg < 604800: # de un día hasta menos de una semana (en 7 días hay 604800 segundos, 86400 * 7)

        dias = num_seg // 86400
        mensaje += (" son " + str(dias) + " días")

        if num_seg % 86400 != 0:
            horas = num_seg % 86400
            mensaje += (" y " + str(horas) + " horas")

            if horas % 60 != 0:
                minutos = horas % 60
                
                if minutos % 60 != 0:
                    segundos = minutos % 60

    print(mensaje)
    



    
        

except ValueError: # Error de que ha introducido letras en lugar de números
    print("Hay que introducir un número valido")