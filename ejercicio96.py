
# Ejercicio 96

# Crear una excepcion que me ayude 
# a determinar si el indice de una 
# lista este fuera de rango

mi_lista = [1,2,3]

try:
    print(mi_lista[5])
except IndexError:
    print("Error, el indice no existe")