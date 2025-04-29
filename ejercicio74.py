
# ejercicio 74

# Crear una clase persona con los atributos:
# nombre, edad, dni
# Con los metodos: 
# init()
# es_mayor_de_edad()

class Persona:

    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
    

persona1 = Persona('Jose', 10, 'QUERTY')

print("El nombre es", persona1.nombre)
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")