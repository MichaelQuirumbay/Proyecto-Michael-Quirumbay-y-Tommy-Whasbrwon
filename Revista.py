##Michael Quirumbay y Tommy Washbrown

from MATERIAL import Material
class Revista(Material):
    contador_revista = 0

    def __init__(self, codigo=None, autor=None, titulo=None, anio=2000, editorial=None, disponible=True,
                 cantidad_disponible=0, tipo=None):
        Material.__init__(self, codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial,
                          disponible=disponible, cantidad_disponible=cantidad_disponible)
        self._tipo = tipo
        Revista.contador_revista += 1
        self._id = Revista.contador_revista

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    def __str__(self):
        return f'Revista:{self.__dict__.__str__()}'

if __name__ == "__main__":
    r = Revista(codigo=45, autor='Michael Quirumbay', titulo='Amigos seremos', editorial='SA Quirumbay', anio=2024,
                disponible=True, cantidad_disponible=2, tipo='Drama')
    print(r)
