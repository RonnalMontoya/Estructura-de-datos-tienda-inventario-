Explicación del Código
Clase Producto:
Atributos:
id_producto: ID único del producto.
nombre: Nombre del producto.
cantidad: Cantidad disponible del producto.
precio: Precio del producto.
Método:
Getters y setters para acceder y modificar los atributos.
__str__: Representa el producto como una cadena de texto.
Clase Inventario:
Atributo:
productos: Lista de productos en el inventario.
Métodos:
agregar_producto: Añade un nuevo producto al inventario, asegurándose de que el ID sea único.
eliminar_producto: Elimina un producto del inventario por su ID.
actualizar_producto: Actualiza la cantidad y/o el precio de un producto por su ID.
buscar_producto_por_nombre: Busca productos por nombre, permitiendo coincidencias parciales.
mostrar_productos: Muestra todos los productos en el inventario.
Interfaz de Usuario:
Función menú:
Crea un menú interactivo en la consola donde el usuario puede realizar todas las operaciones mencionadas: 
Añadir un nuevo producto.
Actualizar la cantidad o el precio de un producto.
Eliminar un producto por su ID.
Buscar productos por nombre. 
Mostrar todos los productos en el inventario.
Salir del programa.
Productos Iniciales:
Se añaden seis productos iniciales al inventario: Margarina, Atun, Aceite, Detergente, Manteca, Leche.
Ejecución del Programa:
El programa se ejecuta a partir de la función menú () en un bucle que permite al usuario realizar múltiples operaciones hasta que decida salir.
