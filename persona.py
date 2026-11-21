
from datetime import date


class Persona:

    def __init__(self, identificacion, nombres, anno_nac,
                 mes_nac, dia_nac, genero, direccion, codigoPostal):

        self.__identificacion = identificacion
        self.__nombres = nombres
        self.__anno_nac = anno_nac
        self.__mes_nac = mes_nac
        self.__dia_nac = dia_nac
        self.__genero = genero
        self.__direccion = direccion
        self.__codigoPostal = codigoPostal

    # GETTERS: permiten consultar los atributos

    def get_identificacion(self):
        return self.__identificacion

    def get_nombres(self):
        return self.__nombres

    def get_anno_nac(self):
        return self.__anno_nac

    def get_mes_nac(self):
        return self.__mes_nac

    def get_dia_nac(self):
        return self.__dia_nac

    def get_genero(self):
        return self.__genero

    def get_direccion(self):
        return self.__direccion

    def get_codigoPostal(self):
        return self.__codigoPostal

    # SETTERS: permiten modificar los atributos

    def set_identificacion(self, identificacion):
        if identificacion.strip():
            self.__identificacion = identificacion
        else:
            raise ValueError("La identificación no puede estar vacía")

    def set_nombres(self, nombres):
        if nombres.strip():
            self.__nombres = nombres
        else:
            raise ValueError("El nombre no puede estar vacío")

    def set_anno_nac(self, anno):
        self.__anno_nac = anno

    def set_mes_nac(self, mes):
        self.__mes_nac = mes

    def set_dia_nac(self, dia):
        self.__dia_nac = dia

    def set_genero(self, genero):
        self.__genero = genero

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_codigoPostal(self, codigo):
        self.__codigoPostal = codigo

    # METODOS PRINCIPALES

    def calcularEdad(self):
        nacimiento = date(
            self.__anno_nac,
            self.__mes_nac,
            self.__dia_nac
        )

        hoy = date.today()

        edad = hoy.year - nacimiento.year

        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        return edad

    def cantidadCitas(self):
        return 0

    def esMayorEdad(self):
        return self.calcularEdad() >= 18
