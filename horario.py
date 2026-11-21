
class Horario:

    DIAS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]

    def __init__(self, dia, hora, disponibilidad, medico):

        if dia not in self.DIAS:
            raise ValueError("Día inválido")

        if not isinstance(hora, int) or not 6 <= hora <= 18:
            raise ValueError("La hora debe estar entre 6 y 18")

        if not isinstance(disponibilidad, bool):
            raise ValueError("La disponibilidad debe ser verdadera o falsa")

        if medico is None:
            raise ValueError("Debe asignarse un médico")

        self.__dia = dia
        self.__hora = hora
        self.__disponibilidad = disponibilidad
        self.__medico = medico

    # GETTERS

    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    def get_disponibilidad(self):
        return self.__disponibilidad

    def get_medico(self):
        return self.__medico

    # SETTERS

    def set_dia(self, dia):
        if dia in self.DIAS:
            self.__dia = dia
        else:
            raise ValueError("Día inválido")

    def set_hora(self, hora):
        if isinstance(hora, int) and 6 <= hora <= 18:
            self.__hora = hora
        else:
            raise ValueError("Hora inválida")

    def set_disponibilidad(self, disponibilidad):
        if isinstance(disponibilidad, bool):
            self.__disponibilidad = disponibilidad
        else:
            raise ValueError("Valor de disponibilidad inválido")

    def set_medico(self, medico):
        if medico is not None:
            self.__medico = medico
        else:
            raise ValueError("Debe asignarse un médico")

    def mostrar_horario(self):
        estado = "Disponible" if self.__disponibilidad else "Ocupado"

        return (
            f"Día: {self.__dia} | "
            f"Hora: {self.__hora}:00 | "
            f"Estado: {estado}"
        )
