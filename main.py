# Se importan las clases de los otros archivos
from Producto import Producto
from Inventario import Inventario


def first_section(actual, lista):

    loop1 = True

    while loop1:
        opcion_secciones = int(input(
            """Estas en la seccion de Inventarios:
            1-Consultar inventario actual
            2-Crear un inventario nuevo
            3-Usar otro inventario
            4-Cambiar nombre del inventario actual
            5-Eliminar inventario actual
            6-Volver
            """))

        if opcion_secciones == 1:
            print(actual.consultar_nombre_inventario())

        elif opcion_secciones == 2:
            name = input('Nombre del inventario: ')
            lista += actual
            actual = Inventario(name)  # Se dispara la clase para asignar un nuevo Inventario

            print(f'Se creo el inventario: {name}')

        elif opcion_secciones == 3:
            print(lista)
            index = int(input('Ingrese un indice: '))
            reemplazo = lista[index]
            lista[index] = actual
            actual = reemplazo

            print('Se esta utlizando el inventario seleccionado')

        elif opcion_secciones == 4:
            actual.name = input('Ingrese un nuevo nombre para el actual: ')

        elif opcion_secciones == 5:
            del actual

        elif opcion_secciones == 6:
            break

        else:
            print('Opcion incorrecta')

    return actual, lista


def creacion_de_inventario():
    print('No se detecto ningun inventario')
    name = input('Nombre del inventario: ')
    inventario = Inventario(name)  # Se dispara la clase para asignar un nuevo Inventario

    print(f'Se creo el inventario: {name}')
    return inventario


# Cuerpo Principal
if __name__ == '__main__':
    ejecutar = True
    inventarios_antiguos = []
    print('- - - RHODOVENTORY 0.1 - - -')

    while ejecutar:
        opcion = int(input(
            """¿Qué vas a hacer?:
            1-Administrar Inventarios
            2-Agregar producto
            3-Ver catalogo
            4-Quitar producto
            5-Salir
            """))

        if opcion == 1:
            try:
                (inventario, inventarios_antiguos) = first_section(inventario, inventarios_antiguos)
            except NameError:
                inventario = creacion_de_inventario()

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

            try:
                # noinspection PyUnboundLocalVariable
                inventario.agregar_producto(producto)
            except NameError as e:
                inventario = creacion_de_inventario()

            print(f'Se creo el producto {nombre_en_catalogo}')

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
