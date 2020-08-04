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
        return self._listado

    def consultar_producto(self, codigo):
        return self._listado[codigo]

    def quitar_producto(self, codigo):
        self._listado.pop(codigo)
