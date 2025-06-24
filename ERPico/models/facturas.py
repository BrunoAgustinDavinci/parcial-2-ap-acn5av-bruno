
class Facturas:
    def __init__(self, name, price, stock,descuento,factura,ticket):
        self.name = name
        self.price = price
        self.stock = stock
        self.descuento = descuento
        self.factura = factura
        self.ticket = ticket
    def __str__(self):
        return f"{self.name} - ${self.price} ({self.stock} en stock)"
