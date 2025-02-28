import os # importa libreria os        
os.system("cls") # Limpia la pantalla

def dibuja_arbol(niveles):
    linea = 20
    num_asteriscos = 1

    for nivel in range(niveles):
        mensaje = " " * (niveles - nivel) + "*"
        
           
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