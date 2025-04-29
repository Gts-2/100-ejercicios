
# ejercicio 72
#crear una clase circulo 

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
Circulo1 = Circulo(5)

print(f"El area es: {Circulo1.calcular_area() }")
print(f"El perimetro es: {Circulo1.calcular_perimetro() }")
