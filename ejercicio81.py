
# ejercicio 81

# Elevar al cuadrado una lista de numeros
# utilizando map()

def cuadrado(X):
    return X ** 2
numeros = [1,2,3,4,5]
cuadrado = list(map(cuadrado, numeros))

print(numeros)
print(cuadrado)
