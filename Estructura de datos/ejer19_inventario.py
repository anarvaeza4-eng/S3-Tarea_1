
class GestorInventario:  
    def __init__(self):  
        self.productos = {}  
      
    def agregar_producto(self, nombre, precio, stock):  
        if precio < 0 or stock < 0:
            raise ValueError("El precio y el stock no pueden ser negativos.")
        self.productos[nombre] = {
            "precio": precio, 
            "stock": stock
        }  
      
    def calcular_valor_total(self):  
        total = 0.0  
        for info in self.productos.values():  
            total += info["precio"] * info["stock"]  
        return total  
      
    def productos_stock_bajo(self, umbral):  
        # Filtra los nombres de los productos cuyo stock es menor al umbral
        return [
            nombre for nombre, info in self.productos.items() 
            if info["stock"] < umbral
        ]


# --- Programa principal de prueba ---
inventario = GestorInventario()

# Registrando productos en el inventario
inventario.agregar_producto("Monitor 24\"", 185.50, 8)
inventario.agregar_producto("Auriculares Inalámbricos", 45.00, 4)
inventario.agregar_producto("Silla Ergonómica", 220.00, 2)
inventario.agregar_producto("Hub USB-C", 30.00, 25)

print(f"Catálogo de productos: {inventario.productos}")

# Calculando el valor monetario global almacenado
valor_global = inventario.calcular_valor_total()
print(f"\nValor total del inventario: ${valor_global:.2f}")

# Consultando productos con stock crítico (menos de 5 unidades)
umbral_critico = 5
print(f"Productos con stock bajo (< {umbral_critico}): {inventario.productos_stock_bajo(umbral_critico)}")