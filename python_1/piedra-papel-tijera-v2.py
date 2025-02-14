"""
LISTA DE MEJORAS

Limitar un máximo de partidas
Contar cuantas veces han ganado, perdido y empatado
Preguntar el nombre del usuario

Guardar los resultados

"""

import os # importa libreria os 
import random # para utilizar numeros aleatorios

os.system("cls") # Limpia la pantalla

# lista de las opciones
# opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ["🥌", "⬜", "✂"]

# variables
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0

# Se pide el nombre al usuario
nombre_usuario = input("Escribe tu nombre --> ")
print(f"Buena suerte {nombre_usuario}!")

while True:
    try:
        numero_partidas = int(input("¿Quantas partidas quieres jugar (entre 1 y 5, 0 para salir)? --> "))
        if numero_partidas == 0:            
            print(f"\nHasta pronto {nombre_usuario}!")           
            # os.system("exit")
            break
        elif 1 <= numero_partidas <= 5: # Si es un numero de partidas correcto
            break # Sale del bucle

        else:
            print("\nHas de introducir un número entre 1 y 5\n")


    except:
        print("\nHas de introducir un número entero\n")

contador_de_partidas = 1 # para que entre en el bucle, si eliges 0 partidas ya no entra

while contador_de_partidas <= numero_partidas:
    contador_de_partidas += 1 # cada vez que juega una partida incrementa en 1 el contador

    # Informar al usuario de las opciones del juego

    menu =f"""
    PIEDRA - PAPEL - TIJERAS
    ========================

    1. {opciones_juego[0]}
    2. {opciones_juego[1]}
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir

    """

    print(menu)

    # Recoger eleccion del usuario

    opcion_humano = input("Elige tu opción --> ").strip()

    if opcion_humano not in ["1","2","3"]:
        print("\nJuego finalizado. Hasta pronto!\n")
    else:
        opcion_pc = str(random.randint(1,3))

        # variable que guarda la elección del jugador y del pc
        resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La maquina ha elegido {opciones_juego[int(opcion_pc)-1]}
    """

        # según el resultado incremento en 1 el contador correspondiente (partidad_ganadas, partidas_perdidas y partidas_empatadas)
        if opcion_humano == opcion_pc:
            print(resultado_partida) # muestra el resultado de la partida actual
            print(f"\t{nombre_usuario} has empatado!!!") # \t es para que haga una tabulación
            partidas_empatadas += 1
        elif (opcion_humano == "1" and opcion_pc == "3") \
            or (opcion_humano == "2" and opcion_pc == "1") \
                or (opcion_humano == "3" and opcion_pc == "2"):
            print(resultado_partida)
            print(f"\t{nombre_usuario} has ganado!!!")
            partidas_ganadas += 1
        else:
            print(resultado_partida)
            print(f"\t{nombre_usuario} has perdido!!!")
            partidas_perdidas += 1

        # en cada partida mostraremos los resultados
        resultado_actual = f"\tGanadas: {partidas_ganadas} | Empates: {partidas_empatadas} | Perdidas: {partidas_perdidas}"
        print(resultado_actual)


print("\nAplicación finalizada\n")
