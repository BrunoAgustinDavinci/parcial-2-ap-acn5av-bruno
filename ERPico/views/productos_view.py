from tkinter import *
from tkinter import ttk


class Ventana:
    def __init__(self, main):
        self.main = main
        self.var_id = StringVar()
        self.nombre = StringVar()
        self.categoria = StringVar()
        self.precio = StringVar()
        self.stock = StringVar()
        self.var_consulta = StringVar()
        self.boton_guardar = Button(main, text="Guardar", command=self.controlador.guardar_modificacion)
        self.boton_alta = Button(main, text="Alta producto", command=self.controlador.alta)
        self.boton_baja = Button(main, text="Baja producto", command=self.controlador.baja)
        self.boton_modificacion = Button(main, text="Modificar producto", command=self.controlador.modificar)
        self.boton_consulta = Button(main, text="Consultar", command=self.controlador.consulta)