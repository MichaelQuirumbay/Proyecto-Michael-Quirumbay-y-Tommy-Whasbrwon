class Libro:
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad, tipo, tapa):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad = cantidad
        self.tipo = tipo
        self.tapa = tapa

    def __str__(self):
        return f"Libro: {self.titulo} ({self.autor}), {self.anio}, {self.editorial}"

class Revista:
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad, numero, categoria):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad = cantidad
        self.numero = numero
        self.categoria = categoria

    def __str__(self):
        return f"Revista: {self.titulo} ({self.autor}), {self.anio}, {self.editorial}, Número {self.numero}"

class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, multas, activo):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.multas = multas
        self.activo = activo

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula}), Email: {self.email}, Teléfono: {self.telefono}"

class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, multas, activo, carrera, nivel, creditos):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, multas, activo)
        self.carrera = carrera
        self.nivel = nivel
        self.creditos = creditos

    def __str__(self):
        return f"Estudiante: {super().__str__()}, Carrera: {self.carrera}, Nivel: {self.nivel}, Créditos: {self.creditos}"

class Docente(Persona):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, multas, activo, departamento, nivel, titulo, posgrado):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, multas, activo)
        self.departamento = departamento
        self.nivel = nivel
        self.titulo = titulo
        self.posgrado = posgrado

    def __str__(self):
        return f"Docente: {super().__str__()}, Departamento: {self.departamento}, Nivel: {self.nivel}, Título: {self.titulo}, Posgrado: {self.posgrado}"

class Pedido:
    def __init__(self, numero, solicitante, materiales, materia, fecha_prestamo, fecha_devolucion):
        self.numero = numero
        self.solicitante = solicitante
        self.materiales = materiales
        self.materia = materia
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f"Pedido {self.numero}: Solicitante {self.solicitante}, Materia {self.materia}, " \
               f"Fecha de Préstamo {self.fecha_prestamo}, Fecha de Devolución {self.fecha_devolucion}"

# Ejemplo de uso
if __name__ == "__main__":
    libro1 = Libro("001", "Autor1", "Titulo1", 2020, "Editorial1", True, 10, 1, "Dura")
    revista1 = Revista("002", "Autor2", "Titulo2", 2021, "Editorial2", True, 5, 1, "Ciencia")

    estudiante1 = Estudiante("1234567890", "Juan", "Perez", "juan@example.com", "0999999999", "Direccion1", 0, True, "Ingenieria", 1, 3)
    docente1 = Docente("0987654321", "Ana", "Gomez", "ana@example.com", "0888888888", "Direccion2", 0, True, "Matematicas", 1, "Pesquero", "Phd")