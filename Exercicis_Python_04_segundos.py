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
    # Definiciones de tiempo
    segundos_por_minuto = 60 # un minuto son 60 segundos
    segundos_por_hora = 3600 # una hora son 60 * 60 = 3600 segundos
    segundos_por_dia = 86400 # un día son 3600 * 24 = 86400 segundos
    segundos_por_semana = 604800 # una semana son 86400 * 7 = 604800 segundos
    # 365 dias de un año son 365 * 86400 = 31536000 segundos
    # 31536000 / 12 = 2628000 segundos en un mes
    segundos_por_mes =  2628000 

    mensaje = "" # guardara el mensaje final con el resultado

    print("Conversor de segundos")
    print("=====================")
    
    # Pido al usuario el numero de segundos
    segundos = int(input("Introduce la cantidad de segundos: "))

    mensaje += f"\n{segundos} segundos son "

    # Cálculos
    # Con la división entera // para que siempre que sea menos de 1 de como resustado 0
    # y el modulo % para ir guardando el resto de segundos

    if segundos < 60:
        mensaje += "menos de 1 minuto"
    else:
        meses = segundos // segundos_por_mes
        segundos = segundos % segundos_por_mes

        semanas = segundos // segundos_por_semana
        segundos = segundos % segundos_por_semana

        dias = segundos // segundos_por_dia
        segundos = segundos % segundos_por_dia

        horas = segundos // segundos_por_hora
        segundos = segundos % segundos_por_hora

        minutos = segundos // segundos_por_minuto
        segundos = segundos % segundos_por_minuto

        
        # Configuro el mensaje final
        if meses != 0:
            mensaje += f"{meses} meses y "

        if semanas != 0:
            mensaje += f"{semanas} semanas y "

        if dias != 0:
            mensaje += f"{dias} días y "

        if horas != 0:
            mensaje += f"{horas} horas y "

        if minutos != 0:
            mensaje += f"{minutos} minutos y "

        if segundos != 0:
            mensaje += f"{segundos} segundos y "
    
    
    print(f"{mensaje}\n") # muestro el mensaje final con el resultado

except ValueError: # Error de que ha introducido letras en lugar de números
    print("\nHay que introducir un número valido\n")