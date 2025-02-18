import os # importa libreria os        
os.system("cls") # Limpia la pantalla

# para crear una clase se utiliza la palabra class
class Persona(): # En la clase principal los parentesisi son optativos
    """
    Propiedades de una persona
    """
    # Atributos son las caracteristicas
    # nombre = None
    # apellido = None
    # funcion = None
    #   
    # METODOS  
    # Los metodos son las funciones dentro de una clase (acciones)

    # Metodo constructor, self hace referencia a la instancia que estas creando
    def __init__(self, nombre, apellido, funcion ): 
        self.nombre = nombre
        self.apellido = apellido
        self.funcion = funcion

    def __str__(self): # Se refiere al propio ojbeto
        # Retorna un string con los datos al utilizar print(nombre_objeto)
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Funcion: {self.funcion}"

# instanciar una clase es crear un objeto de una clase

persona_1 = Persona("Peter", "Parker", "alumno") # crea un objeto de clase persona

print(type(persona_1))
print(persona_1)

print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.funcion)


