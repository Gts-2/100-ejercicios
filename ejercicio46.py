
# ejercicio 46
# solicita al usuario ingresar un 
# numero y cuantos digitos tiene

numero = int(input("Ingrese el numero"))
contador = 0
while numero != 0:
    numero = numero // 10
    contador = contador + 1
print("digitos son |", contador )
