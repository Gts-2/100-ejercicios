
# Ejercicio 92

# Filtrar cadenas de longitud mayor que 3 
# de una lista, usando filter

cadenas = ['python', 'ruby', 'php', 'java']
r = list(filter(lambda x:len(x) > 3, cadenas))

print(r)