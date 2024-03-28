from tkinter import ttk
from tkinter import *
import sqlite3
from recursos.ventana_principal import VentanaPrincipal

if __name__ == '__main__':
    root = Tk() # Instancia de la ventana principal
    app = VentanaPrincipal(root) # Se envia a la clase VentanaPrincipal el
    root.mainloop()