
# ejercicio 71
# Crear una clase rectangulo con los siguientes atributos:
# Base : base del rectangulo
# Altura : altura del rectangulo
# La clase debe tener los siguientes metodos: 
# 





class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
rec1 = Rectangulo(5, 3)

print(f"Area: {rec1.calcular_area()}")
print(f"Perimetro: {rec1.calcular_perimetro()}")