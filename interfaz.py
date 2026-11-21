
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, time

from paciente import Paciente
from medico import Medico
from horario import Horario
from cita import Cita


class CentroSaludApp:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Sistema de Gestión - Centro de Salud")
        self.ventana.geometry("950x700")
        self.ventana.resizable(True, True)

        # Listas principales
        self.pacientes = []
        self.medicos = []
        self.citas = []

        self.crear_interfaz()

    # =====================================
    # CREAR INTERFAZ PRINCIPAL
    # =====================================

    def crear_interfaz(self):

        titulo = tk.Label(
            self.ventana,
            text="CENTRO DE SALUD",
            font=("Arial", 22, "bold"),
            fg="#176B87"
        )
        titulo.pack(pady=15)

        subtitulo = tk.Label(
            self.ventana,
            text="Sistema de gestión de pacientes, médicos y citas",
            font=("Arial", 11)
        )
        subtitulo.pack()

        pestañas = ttk.Notebook(self.ventana)
        pestañas.pack(fill="both", expand=True, padx=15, pady=15)

        self.tab_pacientes = ttk.Frame(pestañas)
        self.tab_medicos = ttk.Frame(pestañas)
        self.tab_horarios = ttk.Frame(pestañas)
        self.tab_citas = ttk.Frame(pestañas)

        pestañas.add(self.tab_pacientes, text="Pacientes")
        pestañas.add(self.tab_medicos, text="Médicos")
        pestañas.add(self.tab_horarios, text="Horarios")
        pestañas.add(self.tab_citas, text="Citas")

        self.crear_tab_pacientes()
        self.crear_tab_medicos()
        self.crear_tab_horarios()
        self.crear_tab_citas()

    # =====================================
    # CAMPO REUTILIZABLE
    # =====================================

    def campo(self, padre, etiqueta, fila):

        tk.Label(
            padre,
            text=etiqueta
        ).grid(
            row=fila,
            column=0,
            padx=10,
            pady=6,
            sticky="w"
        )

        entrada = ttk.Entry(padre, width=30)

        entrada.grid(
            row=fila,
            column=1,
            padx=10,
            pady=6
        )

        return entrada

    # =====================================
    # PACIENTES
    # =====================================

    def crear_tab_pacientes(self):

        frame = self.tab_pacientes

        tk.Label(
            frame,
            text="Registrar paciente",
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=15)

        self.p_id = self.campo(frame, "Identificación:", 1)
        self.p_nombre = self.campo(frame, "Nombres:", 2)
        self.p_anno = self.campo(frame, "Año nacimiento:", 3)
        self.p_mes = self.campo(frame, "Mes nacimiento:", 4)
        self.p_dia = self.campo(frame, "Día nacimiento:", 5)
        self.p_genero = self.campo(frame, "Género:", 6)
        self.p_direccion = self.campo(frame, "Dirección:", 7)
        self.p_codigo = self.campo(frame, "Código postal:", 8)
        self.p_estrato = self.campo(frame, "Estrato:", 9)
        self.p_ciudad = self.campo(frame, "Ciudad:", 10)
        self.p_telefono = self.campo(frame, "Teléfono:", 11)

        ttk.Button(
            frame,
            text="Registrar paciente",
            command=self.registrar_paciente
        ).grid(row=12, column=0, columnspan=2, pady=15)

        self.lista_pacientes = tk.Listbox(
            frame,
            width=75,
            height=8
        )

        self.lista_pacientes.grid(
            row=13,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

    def registrar_paciente(self):

        try:

            paciente = Paciente(
                self.p_id.get().strip(),
                self.p_nombre.get().strip(),
                int(self.p_anno.get()),
                int(self.p_mes.get()),
                int(self.p_dia.get()),
                self.p_genero.get().strip(),
                self.p_direccion.get().strip(),
                int(self.p_codigo.get()),
                int(self.p_estrato.get()),
                self.p_ciudad.get().strip(),
                self.p_telefono.get().strip()
            )

            # Evitar pacientes duplicados

            if any(
                p.get_identificacion() == paciente.get_identificacion()
                for p in self.pacientes
            ):

                raise ValueError("El paciente ya está registrado")

            self.pacientes.append(paciente)

            self.lista_pacientes.insert(
                tk.END,
                f"{paciente.get_identificacion()} - "
                f"{paciente.get_nombres()}"
            )

            # ACTUALIZAR MENUS DESPLEGABLES

            self.actualizar_combos()

            messagebox.showinfo(
                "Registro exitoso",
                "Paciente registrado correctamente"
            )

            # Limpiar campos

            for entrada in [
                self.p_id, self.p_nombre, self.p_anno,
                self.p_mes, self.p_dia, self.p_genero,
                self.p_direccion, self.p_codigo,
                self.p_estrato, self.p_ciudad,
                self.p_telefono
            ]:
                entrada.delete(0, tk.END)

        except Exception as error:

            messagebox.showerror("Error", str(error))

    # =====================================
    # MEDICOS
    # =====================================

    def crear_tab_medicos(self):

        frame = self.tab_medicos

        tk.Label(
            frame,
            text="Registrar médico",
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=15)

        self.m_id = self.campo(frame, "Identificación:", 1)
        self.m_nombre = self.campo(frame, "Nombres:", 2)
        self.m_anno = self.campo(frame, "Año nacimiento:", 3)
        self.m_mes = self.campo(frame, "Mes nacimiento:", 4)
        self.m_dia = self.campo(frame, "Día nacimiento:", 5)
        self.m_genero = self.campo(frame, "Género:", 6)
        self.m_direccion = self.campo(frame, "Dirección:", 7)
        self.m_codigo = self.campo(frame, "Código postal:", 8)

        tk.Label(frame, text="Tipo de médico:").grid(
            row=9, column=0, padx=10, pady=6
        )

        self.m_tipo = ttk.Combobox(
            frame,
            values=["Titular", "Interino", "Sustituto"],
            state="readonly"
        )

        self.m_tipo.grid(row=9, column=1, padx=10, pady=6)
        self.m_tipo.current(0)

        self.m_especialidad = self.campo(
            frame, "Especialidad:", 10
        )

        self.m_sueldo = self.campo(
            frame, "Sueldo mensual:", 11
        )

        ttk.Button(
            frame,
            text="Registrar médico",
            command=self.registrar_medico
        ).grid(row=12, column=0, columnspan=2, pady=15)

        self.lista_medicos = tk.Listbox(
            frame,
            width=75,
            height=8
        )

        self.lista_medicos.grid(
            row=13,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

    def registrar_medico(self):

        try:

            medico = Medico(
                self.m_id.get().strip(),
                self.m_nombre.get().strip(),
                int(self.m_anno.get()),
                int(self.m_mes.get()),
                int(self.m_dia.get()),
                self.m_genero.get().strip(),
                self.m_direccion.get().strip(),
                int(self.m_codigo.get()),
                self.m_tipo.get(),
                self.m_especialidad.get().strip(),
                float(self.m_sueldo.get())
            )

            if any(
                m.get_identificacion() == medico.get_identificacion()
                for m in self.medicos
            ):

                raise ValueError("El médico ya está registrado")

            self.medicos.append(medico)

            self.lista_medicos.insert(
                tk.END,
                f"{medico.get_identificacion()} - "
                f"{medico.get_nombres()} - "
                f"{medico.get_especialidad()}"
            )

            # ACTUALIZAR MENUS

            self.actualizar_combos()

            messagebox.showinfo(
                "Registro exitoso",
                "Médico registrado correctamente"
            )

        except Exception as error:

            messagebox.showerror("Error", str(error))

    # =====================================
    # HORARIOS
    # =====================================

    def crear_tab_horarios(self):

        frame = self.tab_horarios

        tk.Label(
            frame,
            text="Asignar horario médico",
            font=("Arial", 15, "bold")
        ).pack(pady=15)

        tk.Label(frame, text="Médico:").pack()

        self.h_medico = ttk.Combobox(
            frame,
            state="readonly",
            width=40
        )

        self.h_medico.pack(pady=5)

        tk.Label(frame, text="Día:").pack()

        self.h_dia = ttk.Combobox(
            frame,
            values=["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
            state="readonly"
        )

        self.h_dia.pack(pady=5)
        self.h_dia.current(0)

        tk.Label(frame, text="Hora (6 a 18):").pack()

        self.h_hora = ttk.Combobox(
            frame,
            values=list(range(6, 19)),
            state="readonly"
        )

        self.h_hora.pack(pady=5)
        self.h_hora.set("8")

        ttk.Button(
            frame,
            text="Guardar horario",
            command=self.registrar_horario
        ).pack(pady=15)

        self.lista_horarios = tk.Listbox(
            frame,
            width=85,
            height=12
        )

        self.lista_horarios.pack(pady=10)

    def registrar_horario(self):

        try:

            medico = self.buscar_medico(self.h_medico.get())

            if medico is None:
                raise ValueError("Seleccione un médico")

            dia = self.h_dia.get()
            hora = int(self.h_hora.get())

            # Evitar horarios duplicados

            if any(
                h.get_dia() == dia and h.get_hora() == hora
                for h in medico.get_horarios()
            ):

                raise ValueError(
                    "El médico ya tiene registrado ese horario"
                )

            horario = Horario(
                dia,
                hora,
                True,
                medico
            )

            medico.agregar_horario(horario)

            self.lista_horarios.insert(
                tk.END,
                f"{medico.get_nombres()} - "
                f"{horario.mostrar_horario()}"
            )

            messagebox.showinfo(
                "Éxito",
                "Horario registrado correctamente"
            )

        except Exception as error:

            messagebox.showerror("Error", str(error))

    # =====================================
    # CITAS
    # =====================================

    def crear_tab_citas(self):

        frame = self.tab_citas

        tk.Label(
            frame,
            text="Registrar cita médica",
            font=("Arial", 15, "bold")
        ).pack(pady=15)

        tk.Label(frame, text="Paciente:").pack()

        self.c_paciente = ttk.Combobox(
            frame,
            state="readonly",
            width=45
        )

        self.c_paciente.pack(pady=5)

        tk.Label(frame, text="Médico:").pack()

        self.c_medico = ttk.Combobox(
            frame,
            state="readonly",
            width=45
        )

        self.c_medico.pack(pady=5)

        tk.Label(frame, text="Fecha (AAAA-MM-DD):").pack()

        self.c_fecha = ttk.Entry(frame, width=30)
        self.c_fecha.pack(pady=5)

        tk.Label(frame, text="Hora (HH:MM):").pack()

        self.c_hora = ttk.Entry(frame, width=30)
        self.c_hora.pack(pady=5)

        tk.Label(frame, text="Tipo de cita:").pack()

        self.c_tipo = ttk.Combobox(
            frame,
            values=["General", "Odontología", "Especialidad"],
            state="readonly",
            width=30
        )

        self.c_tipo.pack(pady=5)
        self.c_tipo.current(0)

        tk.Label(frame, text="Número de consultorio:").pack()

        self.c_consultorio = ttk.Entry(frame, width=30)
        self.c_consultorio.pack(pady=5)
        self.c_consultorio.insert(0, "NA")

        ttk.Button(
            frame,
            text="Registrar cita",
            command=self.registrar_cita
        ).pack(pady=15)

        self.lista_citas = tk.Listbox(
            frame,
            width=90,
            height=10
        )

        self.lista_citas.pack(pady=10)

    def registrar_cita(self):

        try:

            paciente = self.buscar_paciente(
                self.c_paciente.get()
            )

            medico = self.buscar_medico(
                self.c_medico.get()
            )

            if paciente is None:
                raise ValueError("Debe seleccionar un paciente")

            if medico is None:
                raise ValueError("Debe seleccionar un médico")

            fecha = date.fromisoformat(
                self.c_fecha.get().strip()
            )

            hora = time.fromisoformat(
                self.c_hora.get().strip()
            )

            cita = Cita(
                medico,
                paciente,
                fecha,
                hora,
                self.c_tipo.get(),
                self.c_consultorio.get().strip()
            )

            self.citas.append(cita)

            self.lista_citas.insert(
                tk.END,
                f"{paciente.get_nombres()} | "
                f"{medico.get_nombres()} | "
                f"{fecha} | "
                f"{hora.strftime('%H:%M')}"
            )

            messagebox.showinfo(
                "Cita registrada",
                "La cita se registró correctamente"
            )

        except Exception as error:

            messagebox.showerror("Error", str(error))

    # =====================================
    # ACTUALIZAR MENUS DESPLEGABLES
    # =====================================

    def actualizar_combos(self):

        pacientes = [
            f"{p.get_identificacion()} - {p.get_nombres()}"
            for p in self.pacientes
        ]

        medicos = [
            f"{m.get_identificacion()} - {m.get_nombres()}"
            for m in self.medicos
        ]

        # Actualizar lista de pacientes

        self.c_paciente["values"] = pacientes

        # Actualizar lista de médicos

        self.c_medico["values"] = medicos

        # Actualizar médicos para horarios

        self.h_medico["values"] = medicos

    # =====================================
    # BUSCAR PACIENTES
    # =====================================

    def buscar_paciente(self, seleccion):

        if not seleccion:
            return None

        identificacion = seleccion.split(" - ")[0]

        for paciente in self.pacientes:

            if paciente.get_identificacion() == identificacion:
                return paciente

        return None

    # =====================================
    # BUSCAR MEDICOS
    # =====================================

    def buscar_medico(self, seleccion):

        if not seleccion:
            return None

        identificacion = seleccion.split(" - ")[0]

        for medico in self.medicos:

            if medico.get_identificacion() == identificacion:
                return medico

        return None
