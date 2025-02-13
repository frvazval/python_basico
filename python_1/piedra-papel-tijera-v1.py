
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
opciones_juego = ["Piedra", "Papel", "Tiferas"]
opciones_juego = ["🥌", "⬜", "✂"]

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

    resultado_partida = f"""
    Has elegido {opciones_juego[int(opcion_humano)-1]}
    La maquina ha elegido {opciones_juego[int(opcion_pc)-1]}
"""


    if opcion_humano == opcion_pc:
        print(resultado_partida)
        print("Empate")
    elif (opcion_humano == "1" and opcion_pc == "3") \
        or (opcion_humano == "2" and opcion_pc == "1") \
            or (opcion_humano == "3" and opcion_pc == "2"):
        print(resultado_partida)
        print("Has ganado!!!")
    else:
        print(resultado_partida)
        print("Has perdido!!!")
    

    