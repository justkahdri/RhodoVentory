class Producto:
    def __init__(self, nombre_en_catalogo, codigo, precio, categoria, stock=1):
        self.nombre_en_catalogo = nombre_en_catalogo
        self.codigo = codigo
        self.precio = precio
        self.categoria = categoria
        self.en_stock = stock
