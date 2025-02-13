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
    print("3 - Infantiles : 7.20")

          

def comprar_entradas():
    pass

# Programa principal
entradas = [] # para guardar las entradas compradas

try:

except ValueError:
    print("Has de introducir un número del 1 al 4")

except:
    

mostrar_precios()
