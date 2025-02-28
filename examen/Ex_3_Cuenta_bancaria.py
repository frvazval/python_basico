"""
Programación orientada a objetos: Gestión de cuentas bancarias.

El programa debe:

    Definir la clase Cliente, con los atributos nombre, apellido y edad.

    Definir la clase Banco, con el atributo nombre.
    Incluiremos un método "crear_cuenta" para añadir cuentas.
    Incluiremos un método "eliminar_cuenta" para quitarla del banco.
    Incluiremos el método "mostrar_cuentas" para obtener los datos
    de las diferentes cuentas y el total ingresado en el banco. Ejemplo:
    
    Banco Pasta Bank
    ==============================
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    295310 | Joan    | 4000€
    Total depósitos: 4500.0€
    ==============================


    Definir la clase CuentaBancaria con los atributos titular y saldo.
    Al crear la cuenta bancaria el saldo será 0.
    Incluiremos un número de cuenta mediante un número aleatorio entre
    100000 y 999999.

    Incluir un método ingresar_dinero(...) que permita añadir dinero a la cuenta.
    Deben ser cantidades positivas mayores que cero. En caso contrario mostrar el aviso.
    El mensaje de salida será:
    "Se han depositado [cantidad]€ en la cuenta de [nombre_del_cliente]"

    Incluir un método retirar_dinero(...) que permita retirar dinero de la cuenta, 
    si hay suficiente saldo para ello. En caso contrario, 
    mostrar un mensaje de saldo insuficiente.
    Ejemplo de mensaje: 
    "Se han retirado [cantidad]€ de la cuenta de [nombre_del_cliente]. 
    Saldo actual: [saldo]€"
    Hay que verificar que la cantidad a retirar sea positiva mayor que cero.

    Incluir un método mostrar_saldo_cliente(...) que muestre el saldo actual.
    Así:
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    
     
    Crear al menos 5 cuentas bancarias y utilizar todos 
    los métodos de cada una.

    Nota: no hace falta crear inputs para la entrada de datos.
    Se pueden utilizar directamente los métodos.
"""

import os # importa libreria os        
os.system("cls") # Limpia la pantalla

import random # para utilizar numeros aleatorios

# Creo las clases
class Banco():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.lista_cuentas = [] # Para guardar la cuentas

    # Metodos
    def crear_cuenta(self, cuenta: object):
        # añado la cuenta a la lista de cuentas
        self.lista_cuentas.append(cuenta)
        return f"Se ha creado correctamente la cuenta {cuenta.num_cuenta} en {self.nombre}"


    def eliminar_cuenta(self, cuenta: object):
        if self.lista_cuentas: # Si la lista no esta vacia
           if cuenta in self.lista_cuentas: # Si esta en la lista
               self.lista_cuentas.remove(cuenta)
               return f"la cuenta {cuenta.num_cuenta}, se ha eliminado con exito"
           else: # Si no esta en la lista
               return f"la cuenta {cuenta.num_cuenta}, no se ha podido eliminar porque no existe\n"
               
        else:
            print(f"No hay ninguna cuenta dada de alta en '{self.nombre}', no se puede eliminar")


    def mostrar_cuentas(self):
        if self.lista_cuentas: # Si la lista no esta vacia
            print(f"Listado de cuentas de '{self.nombre}'")
            print("-" * 22)
            for cuenta in self.lista_cuentas:
                print(f"Cuenta: {cuenta.num_cuenta}, Titular: {cuenta.titular.nombre} {cuenta.titular.apellido}")
        else:
            print(f"No hay ninguna cuenta dada de alta en '{self.nombre}'")



class Cliente():
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class CuentaBancaria():
    def __init__(self, titular: object):
        self.titular = titular
        self.saldo = 0
        self.num_cuenta = random.randint(100000, 999999) # Genera un numero aleatorio entre 100000 y 999999

    # Metodos
    def ingresar_dinero(self,cantidad: int):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Se han añadido {cantidad} € al saldo que habia en la cuenta"
        else:
            return "No se puede añadir 0 €"

    def retirar_dinero(self, cantidad: int):
        if cantidad > 0:
            if self.saldo < cantidad: # Si no hay suficiente saldo en la cuenta
                return f"No hay suficiente saldo en la cuenta para retirar {cantidad} €"
            else:
                self.saldo -= cantidad
                return f"Se han retiradoo {cantidad} € del saldo que habia en la cuenta"
        else:
            return "No se puede retirar 0 €"

    def mostrar_saldo_cliente(self):
        return f"El saldo de {self.titular.nombre} {self.titular.apellido} es {self.saldo} €\n"


# Programa principal
# Creo el objeto banco
banco_1 = Banco("Banesto")
banco_2 = Banco("Banco Sabadell")

# Creo los clientes
cliente_1 = Cliente("Antonio", "Perez", 40)
cliente_2 = Cliente("Ana", "Martinez", 30)
cliente_3 = Cliente("Pedro", "Fernandez", 50)

# Creo las cuentas
cuenta_1 = CuentaBancaria(cliente_1)
cuenta_2 = CuentaBancaria(cliente_2)
cuenta_3 = CuentaBancaria(cliente_3)
cuenta_4 = CuentaBancaria(cliente_1)
cuenta_5 = CuentaBancaria(cliente_3)

# Añado las 5 cuentas al banco_1
print(banco_1.crear_cuenta(cuenta_1))
print(banco_1.crear_cuenta(cuenta_2))
print(banco_1.crear_cuenta(cuenta_3))
print(banco_1.crear_cuenta(cuenta_4))
print(banco_1.crear_cuenta(cuenta_5))

# Añado 2 cuentas al banco_2
print(banco_2.crear_cuenta(cuenta_1))
print(banco_2.crear_cuenta(cuenta_5))

# Muestro las cuentas del banco
banco_1.mostrar_cuentas()

# Elimino una cuenta y vuelvo a mostrar la lista de cuentas
print(banco_1.eliminar_cuenta(cuenta_3))
banco_1.mostrar_cuentas()


# Hago un ingreso
print(cuenta_1.ingresar_dinero(3000))
print(cuenta_1.mostrar_saldo_cliente())

# Muestro el saldo de un cliente
print(cuenta_3.mostrar_saldo_cliente())

# Retiro dinero
print(cuenta_1.retirar_dinero(500))
print(cuenta_1.mostrar_saldo_cliente())








