'''
LISTA DE MEJORAS

Limitar un máximo de partidas
Contar cuantas veces han ganado, perdido y empatado
Preguntar el nombre del usuario

Guardar los resultados

'''



import random # Para poder utilizar números aleatorios
import os # Para poder utilizar comandos del sistema
os.system("cls") # Utiliza el comando del sistema cls para borrar la pantalla

# Lista de las opciones
# opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ['🪨','🗒️', '✂️' ] # Lista que contiene las opciones de juego que puede elegir el jugador

# Contadores para saber cuantas partidas ganadas, perdidas o empatadas, han habido despues de jugar el numero de partidas elegido
partidas_ganadas = 0
partidas_perdidas = 0
empates = 0

# Pide el nombre al jugador, para poder personalizar los mensajes
nombre_usuario = input("Escribe tu nombre --> ")
print(f"¡Buena suerte {nombre_usuario}!")

# Bucle que se repetira mientras no se elija un número de partidas valido o la opción 0 para salir
while True:
    try: # Para controlar las excepciones, en caso de error de conversión a entero
        numero_partidas = int(input("¿Cuántas partidas quieres jugar?\n(entre 1 y 5, 0 para salir) --> "))

        # Si se elije 0 sale del juego con un mensaje de despedida
        if numero_partidas == 0:
            print(f"¡Hasta pronto {nombre_usuario}!")
            # os.system("exit"), es para utilizar el comando exit para salir de la aplicación
            # pero no es necesario y por eso esta comentado
            break # Sale del bucle
        elif 1 <= numero_partidas <= 5:
            break # Sale del bucle, con el número de partidas seleccionado
        else:
            # Se muestra en el caso de que se elija una opción incorrecta
            print("Has de introducir un número entre 1 y 5\n")
    except:
        # Se muestra en el caso de que ocurra un error al introducir una letra 
        # y se intente convertir a entero
        print("Has de introducir un número entero\n")


contador_de_partidas = 1 # Se le da el valor 1, porque sino no entraria en el bucle la primera vez

while contador_de_partidas <= numero_partidas:
    contador_de_partidas += 1
    # Informar al usuario de las opciones del juego
    menu = f"""
    PIEDRA - PAPEL - TIJERAS
    ========================

    1. {opciones_juego[0]}
    2. {opciones_juego[1]}
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir

    """

    print(menu) # Se muestra por pantalla el menú que contiena la variable menu

    opcion_humano = input("Elige tu opción --> ").strip()

    if opcion_humano not in ["1","2","3"]:
        print("Juego finalizado. ¡Hasta pronto!")
    else:

        opcion_maquina = str(random.randint(1,3))

        resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La máquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """
        print(resultado_partida)

        if opcion_humano == opcion_maquina:
            empates += 1
            print(f"{nombre_usuario}, habéis empatado")
        elif (opcion_humano=="1" and opcion_maquina=="3") \
            or (opcion_humano=="2" and opcion_maquina=="1") \
                or (opcion_humano=="3" and opcion_maquina=="2"):
            partidas_ganadas += 1
            print(f"{nombre_usuario} has ganado!!!")
        else:
            partidas_perdidas += 1
            print(f"{nombre_usuario} has perdido!!!")

        resultado_actual = f"""
    Ganadas: {partidas_ganadas} | Empates : {empates} | Perdidas : {partidas_perdidas}
        \n\n    
""" 
        print(resultado_actual)

print("\nAplicación finalizada.")
