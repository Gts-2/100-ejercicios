
# ejercicio 59
# Pedir al usuario un numero 
# e imprimir la tabla de multiplicar
# del mismo

numero = int(input("Escribe un numero: "))

for i in range(1, 11):
    resultado = numero * i
    print(F"{numero} x {i} = {resultado}")
