lista_compras = []

def agregar_articulo():
    agg_art = input("Nombre del articulo: ")
    lista_compras.append(agg_art)

def eliminar_articulo():
    print(lista_compras)
    indice = input(int("Seleccione el indice del articulo que desea eliminar: "))
    del lista_compras[indice]

def mostrar_lista():
    print(lista_compras)


while True:
    print("\nMenú")
    print("1. Agregar articulo")
    print("2. Eliminar articulo")
    print("3. Mostrar lista")
    print("4. Salir")

    opción = input("Seleccione una opción (solo numero): ")

    if opción == "1":
        agregar_articulo()
    elif opción == "2":
        eliminar_articulo()
    elif opción == "3":
        mostrar_lista()
    elif opción == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")