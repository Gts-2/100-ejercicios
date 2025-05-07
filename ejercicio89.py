
# ejercicio 89

# Comprobar si una palabra 
# es palindromo usando lambda

palindromo = lambda palabra: palabra == palabra[::-1]

print(palindromo("radar"))
print(palindromo("Python"))