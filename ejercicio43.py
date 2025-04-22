
# ejercicio 43
# solicita al usuario ingresar un 
# numero n e imprime el factorial de
# ese numero
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Ingresa el numero'))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i = i + 1
print('el factorial es', factorial)
