from datetime import datetime, timedelta

class Pedido:
    contador_pedido = 0

    def __init__(self, materia=None, solicitante=None):
        Pedido.contador_pedido += 1
        self._id = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = []
        self._materia = materia
        self._fecha_prestamo = datetime.now()
        td = timedelta(days=5)
        self._fecha_devolucion = self._fecha_prestamo + td

    @property
    def id(self):
        return self._id

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, value):
        self._materia = value

    def agregar_material(self, material):
        self._lista_material.append(material)

    def __str__(self):
        return f"Pedido {self._id}: Materia {self._materia}, Solicitante {self._solicitante}, " \
               f"Fecha de Préstamo {self._fecha_prestamo}, Fecha de Devolución {self._fecha_devolucion}"

# Ejemplo de uso
if __name__ == "__main__":
    pedido1 = Pedido(materia="Sociologia", solicitante="Dannes")
    pedido1.agregar_material("Libro A")
    pedido1.agregar_material("Libro B")

    print(pedido1)
