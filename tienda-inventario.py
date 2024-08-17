# Definición de la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    # Getters y setters para acceder y modificar los atributos de la clase
    def get_id(self):
        return self.id_producto

    def set_id(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not any(p.id_producto == producto.id_producto for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido.")
        else:
            print("Error: El ID ya existe.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        for producto in resultados:
            print(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)


# Función que define el menú de la consola para interactuar con el sistema de inventario
def menu():
    inventario = Inventario()
    inventario.agregar_producto(Producto("0001", "Margarina", 120, 1.70))
    inventario.agregar_producto(Producto("0002", "Atun", 80, 1.15))
    inventario.agregar_producto(Producto("0003", "Aceite", 70, 2.40))
    inventario.agregar_producto(Producto("0004", "Detergente", 56, 1.05))
    inventario.agregar_producto(Producto("0005", "Manteca", 28, 1.65))
    inventario.agregar_producto(Producto("0006", "Leche", 32, 1.25))

    while True:
        print("\n1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                int(nueva_cantidad) if nueva_cantidad else None,
                float(nuevo_precio) if nuevo_precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


# Ejecucutar el programa
if __name__ == "__main__":
    menu()