
# Ejercicio 75

# Crear una clase coche con los atributos:
# marca, modelo, matricula, Km
# con los metodos:
# init como constructor
# avanzar(Km) este aumenta
# el valor de Km en la cantidad


class Coche:
    def __init__(self, marca, modelo,
                 matricula, Km):
        self.marca = marca 
        self.modelo = modelo
        self.matricula = matricula
        self.Km = Km

    
    def avanzar(self, Km):
        self.Km = self.Km + Km

coche1 = Coche('for', 'fiesta', 'ABC DFG', 5000)
print(coche1.__dict__)
coche1.avanzar(3000)
print(coche1.__dict__)