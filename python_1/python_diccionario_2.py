"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar
el proceso sin que se produzca la compra

"""
import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# Definicion de funciones
def mostrar_precios():
    print("Hay tres precios:")
    print("1 - Entrada estandar: 9.00")
    print("2 - Mayores de 65 años (seniors) : 6.00")
    print("3 - Infantiles : 7.20\n") 

             

def comprar_entradas(*argv):
    pass

# Programa principal
# definición de variables, listas, etc...
entradas_compradas = [] # para guardar las entradas compradas
PR_ESTANDAR = 9.00
PR_SENIOR = 6.00
PR_INFANTIL = 7.20
salir = False

try:    
    while not salir:
        mostrar_precios()
        opcion = int(input("Introduce el tipo de entrada que quieres comprar, (4 - para salir): -> "))

        if opcion == 4:
            salir = True

except ValueError:
    print("Has de introducir un número del 1 al 4")

except:
    print("Ha ocurrido un error en el programa")


