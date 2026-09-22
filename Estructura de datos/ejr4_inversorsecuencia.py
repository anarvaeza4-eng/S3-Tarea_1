class InversorSecuencia:
    """Clase para invertir listas mediante bucles manuales y mapear resultados en un diccionario."""
    
    def __init__(self):
        # Diccionario para almacenar el historial de listas originales y sus inversas
        self.historial = {}
    
    def invertir_lista(self, lista):
        """Retorna una nueva lista con los elementos invertidos de forma manual."""
        invertida = []
        # Recorremos desde el último índice hasta el 0 decrementando de a 1
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    
    def invertir_multiples(self, *listas):
        """Procesa múltiples listas utilizando *args y guarda el mapeo en el historial."""
        for l in listas:
            # Convertimos a tupla para usarla como clave en el diccionario
            clave = tuple(l)
            valor = tuple(self.invertir_lista(l))
            self.historial[clave] = valor
        return self.historial


# --- Programa principal de prueba ---
inv = InversorSecuencia()

# Probando inversión individual
secuencia_prueba = ["python", "codigo", "clases"]
print(f"Lista original: {secuencia_prueba}")
print(f"Lista invertida: {inv.invertir_lista(secuencia_prueba)}")

# Probando inversión múltiple con *args
resultado_historial = inv.invertir_multiples([1, 2, 3], ["a", "b"], [10, 20, 30, 40])
print("\nHistorial registrado en el diccionario:")
for original, invertida in resultado_historial.items():
    print(f"Original: {original} -> Invertida: {invertida}")