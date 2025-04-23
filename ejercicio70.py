
# ejercicio 70
# Escribe una funcion para
# clasificar si una sustancia 
# es acida, basica o neutra a 
# partir de su pH

def sustancia(ph):
    if ph < 7:
        return "Acida"
    elif ph > 7:
        return "Basica"
    else: 
        return "Neutra"

resultado = sustancia(7)

print(resultado)