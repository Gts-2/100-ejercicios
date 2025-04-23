
# ejercicio 69
# Escribe una funcion para calcular
# la tasa de desempleo

# td = no_desempleados/fuerza_laboralx100

def tasa_desempleo(no_em, si_em):
    return (no_em / si_em) * 100

resultado = tasa_desempleo(100, 900)

print(resultado)