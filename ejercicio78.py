
# ejercicio 78

# Crear una clase persona y otra clase 
# estudiante

# La clase persona debe tener el atributo nombre
# y el metodo mostrar_nombre()

# La clase estudiante debe heredar de la clase 
# persona y utilizar el metodo mostrar_nombre()
# de la clase persona


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def mostra_nombre(self):
        print(self.nombre)
        
class Estudiante(Persona):
    
     def __init__(self, nombre):
         super().__init__(nombre)
         
     def mostrar(self):    
        super().mostrar_nombre()
         
estudiante1 = Estudiante("Jose")
estudiante1.mostrar()  # Salida: Jose 