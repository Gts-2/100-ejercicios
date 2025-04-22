
# ejercicio 45
# imrime la tabla de multiplicar de 
# un numero ingresado por el usuario

numero = int(input("Ingresa el numero: "))
i = 1
while i <= 10:
    resultado = numero + i
    print(F"{numero} x {i} 0 {numero * i}")
    i += 1