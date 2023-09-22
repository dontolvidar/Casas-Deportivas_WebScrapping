class Apuesta():
    def __init__(self, idapuesta, equipo1, equipo2, categoria_nombre_categoria,tiempo):
        self.idapuesta = idapuesta
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.categoria_nombre_categoria = categoria_nombre_categoria
        self.tiempo=tiempo
    def tolist(self):
        return [self.idapuesta, self.equipo1, self.equipo2, self.categoria_nombre_categoria,self.tiempo]
    
    def get_tiempo(self):
        return self._tiempo

    def set_tiempo(self, tiempo):
        self._tiempo = tiempo

    
    def get_idapuesta(self):
        return self._idapuesta

    def set_idapuesta(self, idapuesta):
        self._idapuesta = idapuesta

    def get_equipo1(self):
        return self._equipo1

    def set_equipo1(self, equipo1):
        self._equipo1 = equipo1

    def get_equipo2(self):
        return self._equipo2

    def set_equipo2(self, equipo2):
        self._equipo2 = equipo2

    def get_categoria_nombre_categoria(self):
        return self._categoria_nombre_categoria

    def set_categoria_nombre_categoria(self, categoria_nombre_categoria):
        self._categoria_nombre_categoria = categoria_nombre_categoria

"""
# Ejemplo de uso
apuesta = Apuesta(0, '', '', '')
print(apuesta.idapuesta)
print(apuesta.equipo1)
print(apuesta.equipo2)
print(apuesta.categoria_nombre_categoria)"""



