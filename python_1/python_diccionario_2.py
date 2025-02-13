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

             

def comprar_entradas(tipo, cant):
    pass

# Programa principal
# definición de variables, listas, etc...
entradas_compradas = [] # para guardar todas las entradas compradas
dic_entradas_compradas = {} # para ir añadiendo nuevas entradas a la lista
PR_ESTANDAR = 9.00
PR_SENIOR = 6.00
PR_INFANTIL = 7.20
salir = False

try:    
    while not salir:
        mostrar_precios()
        opcion = int(input("Introduce el tipo de entrada que quieres comprar, (4 - para salir , 5 - terminar): -> "))

        match opcion:
            case 1:
               tipo = 1
               cantidad = int(input("Cuantas entradas estandar quieres comprar (0 - para salir ): -> "))
               if cantidad > 0:
                   comprar_entradas(tipo, cantidad)
               else:
                   continue              

            case 2:
                tipo = 2
                cantidad = int(input("Cuantas entradas senior quieres comprar (0 - para salir ): -> "))
                if cantidad > 0:                    
                    comprar_entradas(tipo, cantidad)
                else:
                   continue
            case 3:
                tipo = 3
                cantidad = int(input("Cuantas entradas infantiles quieres comprar (0 - para salir ): -> "))
                if cantidad > 0:
                   comprar_entradas(tipo, cantidad)
                else:
                   continue
            case 4:
                salir = True
            case 5:
                pass
            case _:
                print("\nLa opción introducida no es correcta\n")

except ValueError:
    print("\nHas de introducir un número del 1 al 4\n")

except:
    print("\nHa ocurrido un error en el programa\n")


