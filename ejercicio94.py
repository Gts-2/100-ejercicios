
# Ejercicio 94

# Filtrar cadenas que contienen 
# un caracter especifico 
# usando filter

cadenas = ['apple', 'python', 'hola']
caracter = 'h'

con_a = list(filter(lambda x:caracter in x, cadenas))
print(cadenas)
print(con_a)
