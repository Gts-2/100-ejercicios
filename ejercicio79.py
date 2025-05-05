
# Ejercicio 79

# representa una cuenta bancaria 
# condeposito y retiro
# debe haber un titular y un saldo
# Utiliza POO

class cuenta:

    def __init__(self, titutlar, saldo):
        self.titular = titutlar
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Se deposito ", cantidad)

    def retirar(self, cantidad):
        self.saldo -= cantidad
        print("Se retiro ", cantidad)

    def mostrar(self):
        print(self.__dict__)


cuenta1 = cuenta('Roldan', 500)
cuenta1.mostrar()
cuenta1.depositar(1000)
cuenta1.mostrar()
cuenta1.retirar(300)
cuenta1.mostrar()