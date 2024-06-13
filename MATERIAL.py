class Material:
    def __init__(self, codigo=None, autor=None, titulo=None, anio=2000, editorial=None, disponible=True, cantidad_disponible=0):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible
    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible
    @cantidad_disponible.setter
    def  cantidad_disponible(self, cantidad_disponible):
        self._cantidad_disponible= cantidad_disponible

    def __str__(self):
        return f'Material{self.__dict__.__str__()}'

if __name__ == "__main__":
    m = Material(codigo=15, autor='Michael Quirumbay', titulo='La odisea', editorial='SA Quirumbay', anio=2003,
                 disponible=True, cantidad_disponible=5)
    print(m)


