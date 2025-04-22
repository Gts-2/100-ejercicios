
# ejercicio 47
# hacer un menu de opciones que incluye la opcion
# de salir del programa

while True:
    print("1 - sumar")
    print("2 - restar")
    print("3 - sair")

    opcion = int(input("Escribe tu opcion: "))

    if opcion == 1:
        print("Usted esta sumando")
    elif opcion == 2:
        print("Usted esta restando")
    elif opcion == 3:
        break
    else:
        print("No es una opcion valida")

print("Vuelva pronto")