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
    mensaje = f"{num_seg} segundos ->"
    if num_seg < 60: # Hasta menos de un minuto        
        mensaje += " son menos de 1 minuto"
                
    elif num_seg >= 60 and num_seg < 3600: # de un minuto hasta menos de una hora (60 minutos * 60 son 3600 segundos)
        minutos = num_seg // 60
        segundos = num_seg % 60
        mensaje += f" son {minutos} minutos" 
        if segundos != 0: # Si despues de calcular los minutos aun queda algun segundo 
            mensaje += f" y {segundos} segundos"

    elif num_seg >= 3600 and num_seg < 86400: # de una hora a menos de un día (en 24 horas hay 86400 segundos, 60 * 60 * 24)
        horas = num_seg // 3600
        segundos = num_seg % 3600
        
        mensaje  += f" son {horas} horas"  

        # Si después de calcular las horas aun quedan segundos
        if segundos != 0:
            if segundos < 60: # Si son menos de 60 , no llega a un minuto
                mensaje += f" y {segundos} segundos"
            else:
                minutos = segundos // 60 # si son más de 60 calcula los minutos
                if segundos % 60 != 0: # si despues de calcular los minutos, aun queda algun segundo
                    mensaje += f" y {minutos} minutos y {segundos % 60} segundos"
                else:
                    mensaje += f" y {minutos} minutos"
           

    elif num_seg >= 86400 and num_seg < 604800: # de un día hasta menos de una semana (en 7 días hay 604800 segundos, 86400 * 7)       
        dias = num_seg // 86400
        segundos = num_seg % 86400 # segundos restantes despues de calcular los dias
        
        mensaje += f" son {dias} días"

        # Si después de calcular los dias aun quedan segundos
        if segundos != 0:
            if segundos < 3600: # los segundos restantes no llegan a 1 hora
                minutos = segundos // 3600
                seg_restantes = segundos % 3600
                
                mensaje += f" y {minutos} minutos"

                if seg_restantes != 0: # si aun quedan segundos despues de calcular los minutos
                    mensaje += f" y {seg_restantes} segundos"            
            else:
                horas = segundos // 3600 # calcula las horas
                seg_restantes = segundos % 3600

                mensaje += f" y {horas} horas"

                if seg_restantes != 0: # si aun quedan segundos
                    pass

    print(f"\n{mensaje}\n")

        # if segundos < 3600: # los segundos restantes no llegan a 1 hora
        #     minutos = segundos // 3600
        #     seg_restantes = segundos % 3600

        #     if minutos > 0:
        #         mensaje += f" son {minutos} minutos"

        #     if seg_restantes != 0: # Si despues de calcular los minutos aun queda algun segundo 
        #         mensaje += f" y  {seg_restantes} segundos"
        #     else:
        #         horas = segundos // 3600
        #         seg_restantes = segundos % 3600 # segundos que quedan despues de calcular las horas

        #         if horas > 0:
        #             mensaje += f" y {horas} horas"

        #         if seg_restantes != 0: # si despues de calcular las horas aun quedan segundos
        #             if seg_restantes < 60: # Si son menos de 60 , no llega a un minuto
        #                 mensaje += f" y {seg_restantes} segundos"
        #         else:
        #             minutos = seg_restantes // 60 # si son más de 60 calcula los minutos
        #             if seg_restantes % 60 != 0: # si despues de calcular los minutos, aun queda algun segundo
        #                 mensaje += f" y {minutos} minutos y {seg_restantes % 60} segundos"                     

    # muestra por pantalla el mensaje final
    
    



    
        

except ValueError: # Error de que ha introducido letras en lugar de números
    print("Hay que introducir un número valido")