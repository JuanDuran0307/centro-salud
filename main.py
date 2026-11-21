
import tkinter as tk
from interfaz import CentroSaludApp


def iniciar_sistema():

    ventana = tk.Tk()

    aplicacion = CentroSaludApp(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    iniciar_sistema()
