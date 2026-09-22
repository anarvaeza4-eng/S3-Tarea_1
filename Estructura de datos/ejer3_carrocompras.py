class CarroCompras:
    """Clase para gestionar un carro de compras usando diccionarios."""
    
    def __init__(self):
        # Diccionario para almacenar nombre -> precio
        self.articulos = {}
    
    def agregar_articulo(self, nombre, precio):
        """Agrega o actualiza un artículo en el diccionario del carrito."""
        self.articulos[nombre] = precio
    
    def total_carrito(self):
        """Retorna la suma de todos los precios de los artículos."""
        return sum(self.articulos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        """Retorna una lista de artículos cuyos precios están dentro del rango."""
        filtrados = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                filtrados.append(nombre)
        return filtrados


# --- Programa principal de prueba ---
mi_carrito = CarroCompras()

# Agregando artículos
mi_carrito.agregar_articulo("pan", 2.50)
mi_carrito.agregar_articulo("leche", 3.00)
mi_carrito.agregar_articulo("carne", 12.00)

# Probando total y filtros
print(f"Total del carrito: ${mi_carrito.total_carrito()}")
print(f"Artículos económicos (entre 2 y 5): {mi_carrito.articulos_por_rango(2.00, 5.00)}")