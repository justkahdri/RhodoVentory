# Se importan las clases de los otros archivos
from Inventario import Inventario
from Producto import Producto

# Cuerpo Principal
if __name__ == '__main__':
    ejecutar = True
    print('- - - RHODOVENTORY 0.1 - - -')

    while ejecutar:
        opcion = int(input(
            """¿Qué vas a hacer?:
            1-Crear Inventario
            2-Agregar producto
            3-Ver catalogo
            4-Quitar producto
            5-Salir
            """))

        if opcion == 1:
            nombre = input('Nombre del inventario: ')
            inventario = Inventario(nombre)     # Se dispara la clase para asignar un nuevo Inventario

            print(f'Se creo el inventario: {nombre}')

        elif opcion == 2:
            nombre_en_catalogo = input('Nombre de venta: ')
            codigo = input('Codigo de Identificacion: ')
            precio = input('Precio: ')
            categoria = input('Categoria: ')
            stock = input('Cantidad(opcional): ')

            # Se asigna una cantidad de stock por defecto
            if stock == '':
                stock = 1
            else:
                stock = int(stock)

            producto = Producto(nombre_en_catalogo, codigo, precio, categoria, stock)
            print(f'Se creo el producto {nombre_en_catalogo}')
        #    inventario = input('Especifique un inventario: ')
            inventario.agregar_producto(producto)

        elif opcion == 3:
            print('Catalogo de productos: ')
            for i in inventario.consultar_productos():
                print(i)

        elif opcion == 4:
            codigo = input('Codigo del producto a eliminar: ')
            inventario.quitar_producto(codigo)

        elif opcion == 5:
            ejecutar = False

        else:
            print('Opcion incorrecta')
