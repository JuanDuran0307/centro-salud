
from datetime import date, time


class Cita:

    TIPOS = ["General", "Odontología", "Especialidad"]

    DIAS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]

    def __init__(self, medico, paciente, fecha, hora,
                 tipo, numConsultorio="NA"):

        if medico is None or paciente is None:
            raise ValueError("Debe seleccionar médico y paciente")

        if not isinstance(fecha, date):
            raise ValueError("La fecha debe ser válida")

        if not isinstance(hora, time):
            raise ValueError("La hora debe ser válida")

        if fecha < date.today():
            raise ValueError("No se pueden registrar citas pasadas")

        if tipo not in self.TIPOS:
            raise ValueError("Tipo de cita inválido")

        # Convertimos el día al formato del horario
        dia = self.DIAS[fecha.weekday()]

        # Consultamos disponibilidad
        horarios = medico.verificarDisponibilidad(
            dia, hora.hour
        )

        if not horarios:
            raise ValueError("El médico no está disponible")

        self.__medico = medico
        self.__paciente = paciente
        self.__fecha = fecha
        self.__hora = hora
        self.__tipo = tipo
        self.__numConsultorio = numConsultorio

        # Ocupamos el horario
        horarios[0].set_disponibilidad(False)

        # Relacionamos la cita con el médico y paciente
        medico.agregar_cita(self)
        paciente.agregar_cita(self)
        paciente.set_medico(medico)

    # GETTERS

    def get_medico(self):
        return self.__medico

    def get_paciente(self):
        return self.__paciente

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_tipo(self):
        return self.__tipo

    def get_numConsultorio(self):
        return self.__numConsultorio

    # SETTERS

    def set_tipo(self, tipo):
        if tipo in self.TIPOS:
            self.__tipo = tipo
        else:
            raise ValueError("Tipo de cita inválido")

    def set_numConsultorio(self, numero):
        self.__numConsultorio = numero

    # CONSULTAS

    def consultarMedico(self):
        return self.__medico

    def consultarPaciente(self):
        return self.__paciente

    def mostrar_informacion(self):
        return (
            f"Paciente: {self.__paciente.get_nombres()}\n"
            f"Médico: {self.__medico.get_nombres()}\n"
            f"Especialidad: {self.__medico.get_especialidad()}\n"
            f"Fecha: {self.__fecha}\n"
            f"Hora: {self.__hora.strftime('%H:%M')}\n"
            f"Tipo: {self.__tipo}\n"
            f"Consultorio: {self.__numConsultorio}"
        )
