class Inventario:

    def __init__(self, nombre):
        self.nombre = nombre
        self._listado = []

    def consultar_nombre_inventario(self):
        return self.nombre

    def agregar_producto(self, producto):
        nuevo_producto = {
            'Nombre de Catalogo': producto.nombre_en_catalogo,
            'ID': producto.codigo,
            'Precio': producto.precio,
            'Categoria': producto.categoria,
            'Cant. en Stock': producto.en_stock
        }
        self._listado.append(nuevo_producto)

    def consultar_productos(self):
        for i in self._listado:
            if not isinstance(i, dict):
                del i
                continue
            pretty(i)

    def consultar_producto(self, codigo):
        return self._listado[codigo]

    def quitar_producto(self, codigo):
        for i in range(len(self._listado)):
            if self._listado[i]['ID'] == codigo:
                del self._listado[i]
                break
        print(f'El producto con el codigo {codigo} fue eliminado con exito')


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key) + ' :')
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))
