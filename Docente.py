from Persona import Persona

class Docente(Persona):
    contador_docente = 0

    def _init_(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None, direccion=None, numero_libro=198, activo=3, carrera=None, id=1, titulo_3er_nivel=3, titulo_4to_nivel=4):

        Persona._init_(self, cedula, nombre, apellido, email, telefono, direccion, numero_libro, activo, carrera)

        self._id = id
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, value):
        self._titulo_3er_nivel = value

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, value):
        self._titulo_4to_nivel = value

    def _str_(self):
        return f'Docente:{self._dict.str_()}'

    def pedir_libro(self):
        print(f"Docente{self.nombre} ha pedido un libro.")
        pass

    def devolver_libro(self):
        print(f"Docente{self.nombre} ha devuelto un libro.")
        pass

if __name__ == '__main__':

 d = Docente("01245785487", "Michael", "Quirumbay", "itsmichaelqui@gmail.com", "0914659684", "Cristo del consuelo",15, 10, "matematicas")
 print(d)
 print(Docente.mro())