
from persona import Persona


class Paciente(Persona):

    def __init__(self, identificacion, nombres, anno_nac,
                 mes_nac, dia_nac, genero, direccion, codigoPostal,
                 estrato, ciudad, telefono):

        # Llamamos al constructor de Persona
        super().__init__(
            identificacion, nombres, anno_nac,
            mes_nac, dia_nac, genero, direccion, codigoPostal
        )

        # Atributos propios del paciente
        if not isinstance(estrato, int) or not 0 <= estrato <= 6:
            raise ValueError("El estrato debe estar entre 0 y 6")

        if not ciudad.strip():
            raise ValueError("La ciudad es obligatoria")

        if not telefono.strip():
            raise ValueError("El teléfono es obligatorio")

        self.__estrato = estrato
        self.__ciudad = ciudad
        self.__telefono = telefono

        # Listas para almacenar información
        self.__citas = []
        self.__medico = None
        self.__cantidadCitasPorMes = []
        self.__cantidadCitasPorEsp = []

    # GETTERS

    def get_estrato(self):
        return self.__estrato

    def get_ciudad(self):
        return self.__ciudad

    def get_telefono(self):
        return self.__telefono

    def get_citas(self):
        return self.__citas

    def get_medico(self):
        return self.__medico

    def get_cantidadCitasPorMes(self):
        return self.__cantidadCitasPorMes

    def get_cantidadCitasPorEsp(self):
        return self.__cantidadCitasPorEsp

    # SETTERS

    def set_estrato(self, estrato):
        if isinstance(estrato, int) and 0 <= estrato <= 6:
            self.__estrato = estrato
        else:
            raise ValueError("Estrato inválido")

    def set_ciudad(self, ciudad):
        if ciudad.strip():
            self.__ciudad = ciudad
        else:
            raise ValueError("La ciudad es obligatoria")

    def set_telefono(self, telefono):
        if telefono.strip():
            self.__telefono = telefono
        else:
            raise ValueError("El teléfono es obligatorio")

    def set_medico(self, medico):
        self.__medico = medico

    # METODOS

    def agregar_cita(self, cita):
        self.__citas.append(cita)

    def cantidadCitas(self):
        return len(self.__citas)

    def mostrar_informacion(self):
        return (
            f"Paciente: {self.get_nombres()}\n"
            f"Identificación: {self.get_identificacion()}\n"
            f"Ciudad: {self.__ciudad}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Estrato: {self.__estrato}\n"
            f"Cantidad de citas: {self.cantidadCitas()}"
        )
