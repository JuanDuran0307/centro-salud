# centro-salud
# 🏥 Sistema de Gestión – Centro de Salud

## 📌 Descripción del proyecto

El Sistema de Gestión de Centro de Salud es una aplicación de escritorio desarrollada en Python, utilizando programación orientada a objetos (POO) y la librería Tkinter para la creación de su interfaz gráfica.

El sistema permite gestionar la información de pacientes y médicos, registrar horarios de atención y administrar citas médicas, facilitando la organización de los servicios de un centro de salud.

Este proyecto fue desarrollado como parte del Taller 5 de Programación Orientada a Objetos, con el propósito de aplicar conceptos fundamentales de POO en una situación práctica.

## 🎯 Objetivo general

Desarrollar un sistema de gestión para un centro de salud mediante Python y programación orientada a objetos, que permita registrar pacientes, médicos, horarios y citas médicas, aplicando principios de organización, reutilización y encapsulamiento del código.

## ⚙️ Funcionalidades principales

- **Registro de pacientes:** permite ingresar información personal y datos de contacto.
- **Registro de médicos:** permite almacenar información de los profesionales, especialidad y tipo de vinculación.
- **Gestión de horarios:** permite asignar días y horas de atención a cada médico.
- **Registro de citas:** permite relacionar pacientes con médicos y programar citas.
- **Validación de fechas:** evita registrar citas en fechas anteriores al día actual.
- **Validación de disponibilidad:** verifica que el médico tenga un horario disponible antes de registrar una cita.
- **Control de citas:** almacena las citas asociadas a cada paciente y médico.

## 🧠 Conceptos de programación orientada a objetos aplicados

Durante el desarrollo del proyecto se implementaron los siguientes conceptos:

- **Clases y objetos:** permiten representar los elementos principales del centro de salud.
- **Herencia:** las clases Paciente y Medico heredan de la clase Persona.
- **Encapsulamiento:** se utilizan atributos privados para proteger la información de los objetos.
- **Polimorfismo:** se implementa mediante la redefinición del método `cantidadCitas()` en las clases correspondientes.
- **Relaciones entre objetos:** las citas relacionan pacientes y médicos, mientras que los horarios pertenecen a los médicos.
- **Listas:** permiten almacenar múltiples pacientes, médicos, horarios y citas.

## 🗂️ Estructura del proyecto

```text
CentroSalud/
│
├── persona.py       # Clase base Persona
├── paciente.py      # Clase Paciente
├── medico.py        # Clase Medico
├── horario.py       # Clase Horario
├── cita.py          # Clase Cita
├── interfaz.py      # Interfaz gráfica con Tkinter
├── main.py          # Archivo principal del programa
└── README.md        # Documentación del proyecto
```

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.
- **Interfaz gráfica:** Tkinter.
- **Editor de código:** Visual Studio Code.
- **Control de versiones:** Git y GitHub.

## 💻 Requisitos para ejecutar el proyecto

- Tener instalado Python 3.
- Contar con un editor de código o terminal.
- Tener Git instalado (opcional, para clonar el repositorio).

Tkinter normalmente viene incluido en la instalación estándar de Python para Windows.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone URL_DE_TU_REPOSITORIO
```

### 2. Entrar a la carpeta del proyecto

```bash
cd CentroSalud
```

### 3. Ejecutar el programa

```bash
python main.py
```

También puedes ejecutar el archivo `main.py` directamente desde Visual Studio Code.

## 📋 Uso del sistema

1. Ejecutar el archivo `main.py`.
2. Ingresar a la pestaña Pacientes y registrar un paciente.
3. Ingresar a la pestaña Médicos y registrar un médico.
4. Acceder a Horarios y asignar un día y una hora disponible al médico.
5. Ingresar a Citas, seleccionar el paciente y el médico, e indicar la fecha, hora y tipo de cita.
6. El sistema verificará la disponibilidad antes de guardar la cita.

**Nota:** para registrar una cita correctamente, el médico debe tener previamente un horario disponible que coincida con el día y la hora seleccionados.

## 👨‍💻 Autor

**Nombre:** [Escribe tu nombre completo]

**Asignatura:** Programación Orientada a Objetos

**Proyecto:** Taller 5 – Sistema de Gestión Centro de Salud

**Institución:** [Nombre de tu institución educativa]

## 📚 Conclusión

Este proyecto permitió fortalecer los conocimientos sobre programación orientada a objetos mediante el desarrollo de una aplicación práctica. Además, permitió comprender cómo organizar un programa en diferentes clases, establecer relaciones entre objetos y construir una interfaz gráfica utilizando Python y Tkinter.

---

**Proyecto académico desarrollado con fines educativos.**


