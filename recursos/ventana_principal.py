import tkinter as tk
from tkinter import *
from tkinter.ttk import Treeview,Style
import sqlite3


class VentanaPrincipal:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("App Gestor de Produtos") # Titulo de la ventana
        self.ventana.resizable(1,1) # Activar la redimension de la ventana. Para
        desactivarla: (0,0)
        self.ventana.wm_iconbitmap('recursos/python.ico')
        frame = LabelFrame(self.ventana, text="Registrar un nuevo Producto")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        self.etiqueta_nombre = Label(frame, text="Nombre: ")  # Etiqueta de texto ubicada
        self.etiqueta_nombre.grid(row=1, column=0)  # Posicionamiento a traves de grid
        # Entry Nombre (caja de texto que recibira el nombre)
        self.nombre = Entry(frame)  # Caja de texto (input de texto) ubicada en el frame
        self.nombre.focus()  # Para que el f
        self.nombre.grid(row=1, column=1)

        self.etiqueta_precio = Label(frame, text="Precio: ")  # Etiqueta de texto ubicada
        self.etiqueta_precio.grid(row=2, column=0)
        # Entry Precio (caja de texto que recibira el precio)
        self.precio = Entry(frame)  # Caja de texto (input de texto) ubicada en el frame
        self.precio.grid(row=2, column=1)

        self.boton_aniadir = Button(frame, text="Guardar Producto")
        self.boton_aniadir.grid(row=3, columnspan=2, sticky=W + E)

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri',11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky':'nswe'})])

        self.tabla = Treeview(height = 20, columns = 2, style="mystyle.Treeview")
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'Nombre', anchor = CENTER) # Encabezado 0
        self.tabla.heading('#1', text='Precio', anchor = CENTER) # Encabezado 1
        #self.get_productos()

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    def get_productos(self):
        registros_tabla = self.tabla.get_children()
        for fila in registros_tabla:
            self.tabla.delete(fila)

        query = 'SELECT * FROM producto ORDER BY nombre DESC'
        registros_db = self.db_consulta(query)
        for fila in registros_db:
            print(fila)
            self.tabla.insert('', 0, text=fila[1], values=fila[2])