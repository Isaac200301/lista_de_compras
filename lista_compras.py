lista_compras = []

def agregar_articulo():
    while True:
        agg_art = input("Nombre del articulo: ")
        lista_compras.append(agg_art)
        decision = input("¿Quiere seguir agregando? y/n: ")
        if decision == "n":
            break

def eliminar_articulo():
    print(lista_compras)
    indice = int(input("Seleccione el indice del articulo que desea eliminar: "))
    del lista_compras[indice + 1] #indice mas uno para que no exista la posicion cero

def mostrar_lista():
    print(lista_compras)


while True:
    print("\nMenú")
    print("1. Agregar articulo")
    print("2. Eliminar articulo")
    print("3. Mostrar lista")
    print("4. Salir")

    opción = int(input("Seleccione una opción (solo numero): "))

    if opción == 1:
        agregar_articulo()
    elif opción == 2:
        eliminar_articulo()
    elif opción == 3:
        mostrar_lista()
    elif opción == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")