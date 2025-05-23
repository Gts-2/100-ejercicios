class Persona:
     def __init__(self, nombre=None, edad=None):
         self._nombre = nombre
         self._edad = edad
         
     @property  
     def nombre(self):
         return self._nombre
     
     @nombre.setter 
     def nombre(self, nuevo_nombre):
         self._nombre = nuevo_nombre
         
     @property   
     def edad(self):
         return self._edad
     
     @edad.setter
     def edad(self, nueva_edad):
         self._edad = nueva_edad
         
     def mostrar(self):
         print(self.__dict__)
         
     def esMayorDeEdad(self):
         if self._edad >= 18: 
             print("Es mayor de edad")   
             return True
         else:       
             print("Es menor de edad")  
             return False
 
Persona1 = Persona("Juan", 15)
Persona1.esMayorDeEdad()
Persona1.mostrar()