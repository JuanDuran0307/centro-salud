
from persona import Persona


class Medico(Persona):

    def __init__(self, identificacion, nombres, anno_nac,
                 mes_nac, dia_nac, genero, direccion, codigoPostal,
                 tipoMedico, especialidad, sueldo):

        super().__init__(
            identificacion, nombres, anno_nac,
            mes_nac, dia_nac, genero, direccion, codigoPostal
        )

        tipos_validos = ["Titular", "Interino", "Sustituto"]

        if tipoMedico not in tipos_validos:
            raise ValueError("Tipo de médico inválido")

        if not especialidad.strip():
            raise ValueError("La especialidad es obligatoria")

        if sueldo < 0:
            raise ValueError("El sueldo no puede ser negativo")

        self.__tipoMedico = tipoMedico
        self.__especialidad = especialidad
        self.__sueldo = sueldo
        self.__citas = []
        self.__horarios = []

    # GETTERS

    def get_tipoMedico(self):
        return self.__tipoMedico

    def get_especialidad(self):
        return self.__especialidad

    def get_sueldo(self):
        return self.__sueldo

    def get_citas(self):
        return self.__citas

    def get_horarios(self):
        return self.__horarios

    # SETTERS

    def set_tipoMedico(self, tipo):
        if tipo in ["Titular", "Interino", "Sustituto"]:
            self.__tipoMedico = tipo
        else:
            raise ValueError("Tipo de médico inválido")

    def set_especialidad(self, especialidad):
        if especialidad.strip():
            self.__especialidad = especialidad
        else:
            raise ValueError("Especialidad obligatoria")

    def set_sueldo(self, sueldo):
        if sueldo >= 0:
            self.__sueldo = sueldo
        else:
            raise ValueError("Sueldo inválido")

    # METODOS

    def CalcularSueldoAnual(self):
        return self.__sueldo * 12

    def cantidadCitas(self):
        return len(self.__citas)

    def agregar_cita(self, cita):
        self.__citas.append(cita)

    def agregar_horario(self, horario):
        self.__horarios.append(horario)

    def verificarDisponibilidad(self, dia, hora):
        disponibles = []

        for horario in self.__horarios:

            if (horario.get_dia() == dia
                    and horario.get_hora() == hora
                    and horario.get_disponibilidad()):

                disponibles.append(horario)

        return disponibles

    def mostrar_informacion(self):
        return (
            f"Médico: {self.get_nombres()}\n"
            f"Identificación: {self.get_identificacion()}\n"
            f"Especialidad: {self.__especialidad}\n"
            f"Tipo: {self.__tipoMedico}\n"
            f"Sueldo mensual: ${self.__sueldo}\n"
            f"Sueldo anual: ${self.CalcularSueldoAnual()}\n"
            f"Cantidad de citas: {self.cantidadCitas()}"
        )
