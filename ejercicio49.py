
# ejercicio 49
# simular un lanzamiento 
# de dado hasta obtener un 6

import random
numero = 0
while numero != 6:
    numero = random.randint(1, 6)
    print(F"Haz sacado un  {numero}")

print("sacaste un 6")
