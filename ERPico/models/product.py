
class Product:
    def __init__(self, name, price, stock,descuento):
        self.name = name
        self.price = price
        self.stock = stock
        self.descuento = descuento

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.stock} en stock)"
