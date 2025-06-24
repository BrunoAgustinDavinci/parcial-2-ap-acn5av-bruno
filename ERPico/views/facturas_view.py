
def render_home():
    print("FACTURAS")
from tkinter import *
from tkinter import ttk


class FACTURAS:
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
        self.label_stock = Label(main,text="Stock", command=self.controlador.stock)
        