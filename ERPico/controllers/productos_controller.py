from tkinter import Tk
from tkinter.messagebox import showinfo, showerror, askyesno

class Controlador:
    def __init__(self, vista):
        self.vista = vista
  

    def alta(self):
        patron = self.regex.validar_producto()
        patron_categoria = self.regex.validar_categoria()
        nombre = self.vista.nombre.get().strip()
        categoria = self.vista.categoria.get().strip()
        precio = self.vista.precio.get()
        stock = self.vista.stock.get()