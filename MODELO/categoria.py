class Categoria():
    def __init__(self, nombre_categoria):
        self._nombre_categoria = nombre_categoria

    def get_nombre_categoria(self):
        return self._nombre_categoria

    def set_nombre_categoria(self, nuevo_nombre_categoria):
        self._nombre_categoria = nuevo_nombre_categoria

    def tolist(self):
        return [self._nombre_categoria]
    
# Ejemplo de uso
#categoria = Categoria("Electrónica")
#print(categoria.nombre_categoria)  # Imprime "Electrónica"