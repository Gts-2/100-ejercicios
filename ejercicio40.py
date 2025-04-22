
# ejercicio 40
# calcular el IMC e interpretalo

peso = 70
altura = 1.75

imc = peso / (altura**2)
print(imc)

if imc < 18.5:
    print('Bajo peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidad grado I')
elif imc < 40:
    print('Obesidad grado II')
else:
    print('Obesidad grado III')