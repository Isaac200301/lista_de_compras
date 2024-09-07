# Proyecto: Lista de Compras

Este es un programa simple en Python que permite al usuario gestionar una lista de compras a través de un menú interactivo. El programa permite agregar, eliminar y mostrar los artículos en la lista de compras.

## Funcionalidades

1. **Agregar artículo**: Permite al usuario agregar artículos a la lista.
2. **Eliminar artículo**: Permite al usuario eliminar un artículo de la lista utilizando el índice del artículo.
3. **Mostrar lista**: Muestra todos los artículos agregados a la lista.
4. **Salir**: Cierra el programa.

## Instrucciones de Uso

1. Clona el repositorio o descarga el archivo con el código.
2. Ejecuta el archivo Python en tu terminal o entorno preferido.
      
      ```bash
   python lista_compras.py

### Detalles de las 

**agregar_articulo():**

Solicita el nombre del artículo para agregarlo a la lista.
El usuario puede seguir agregando artículos hasta que indique que no quiere continuar (y/n).

**eliminar_articulo():**

Muestra los artículos de la lista junto con su índice.
Solicita al usuario que seleccione el índice del artículo a eliminar.
**Nota:** El índice tiene un error en la línea del lista_compras[indice + 1]. Debe corregirse a del lista_compras[indice] para evitar errores de rango fuera de índice.

**mostrar_lista():**

Muestra todos los artículos en la lista.

**Menú principal:**

Presenta las opciones para ejecutar cada función.

#### Consideraciones
El código no maneja casos donde el usuario ingrese un índice no válido en la opción de eliminar artículo.
No hay validación para entradas incorrectas en el menú.
El programa se ejecutará indefinidamente hasta que el usuario seleccione la opción de salir (4).