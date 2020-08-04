class Inventario:

    def __init__(self, nombre):
        self.nombre = nombre
        self._listado = []

    def consultar_nombre_inventario(self):
        return self.nombre

    def agregar_producto(self, producto):
        self._listado.append({
            producto.nombre_en_catalogo,
            producto.codigo,
            producto.precio,
            producto.categoria,
            producto.en_stock
        })

    def consultar_productos(self):
        return self._listado

    def consultar_producto(self, codigo):
        return self._listado[codigo]

    def quitar_producto(self, codigo):
        self._listado.pop(codigo)
