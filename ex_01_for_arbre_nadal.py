import os # importa libreria os        
os.system("cls") # Limpia la pantalla

def dibuja_arbol(niveles):
    linea = 20
    num_asteriscos = 1 # Asteriscos de la primaera linea

    for nivel in range(niveles):
        mensaje = " " * (niveles - nivel)

        if nivel != 0: # Si no es la primera linea
            num_asteriscos = (nivel * 2) + 1
            mensaje += "*" * num_asteriscos
        else: # Si es la primera linea
            mensaje += "*"        
           
        print(mensaje)       

try:
    continuar = True
    while continuar:
        niveles = int(input("¿Cuantos niveles tendra el arbol de Navidad? (entre 5 y 10) -> "))
        if 5 <= niveles <= 10:
            continuar = False
        else: 
            print("Se tiene que elegir un valor entre 5 y 10\n")
    dibuja_arbol(niveles)

except ValueError:
    print("Se tiene que introducir un número, no se pueden poner letras\n")