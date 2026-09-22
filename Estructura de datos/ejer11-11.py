class Factura:
    def __init__(self):
        self.items = []  # [(producto, cantidad, precio_unitario)]

    def agregar_item(self, producto, cantidad, precio):
        self.items.append((producto, cantidad, precio))

    def agregar_items(self, *items):
        for producto, cantidad, precio in items:
            self.agregar_item(producto, cantidad, precio)

    def subtotal(self):
        return sum(cantidad * precio for _, cantidad, precio in self.items)

    def total_con_iva(self, iva=0.15):
        return round(self.subtotal() * (1 + iva), 2)

    def item_mas_caro(self):
        return max(self.items, key=lambda item: item[1] * item[2])[0]

f = Factura()
f.agregar_items(("Cuaderno", 4, 2.50), ("Lápiz", 10, 0.50), ("Mochila", 1, 25.00))
print(f.subtotal())                                        # 40.0
print(f.total_con_iva())                                   # 46.0
print(f.item_mas_caro())                                   # 'Mochila'