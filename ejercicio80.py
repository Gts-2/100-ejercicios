
# ejercicio 80

# Obtener la cantidad de memoria ram
# en mi computadora o laptop
# pip istall psutil

import psutil

def Obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria_total / (1024 ** 3)
    return memoria_total

memoria = Obtener_ram()

print('Total de ram ', memoria, 'GB')
