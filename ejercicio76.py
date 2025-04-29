
# ejercicio 76

# Crear una clase de animal con los atributos:
# especie ynombre
# La clase debe tener los metodos:
# init y hablar()
# el metodo hablar nos retorna una palabra
# segun la interpretacion del sonido como un perro
# seria "guau"

class Animal:

    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        if self.especie == 'perro':
            print("Guau")
        elif self.especie  == 'gato':
            print("Miau")
        else:
            print("animal no detectado")

perro = Animal('perro', 'solovino')
gato = Animal('gato', 'gato')

perro.hablar()
gato.hablar()