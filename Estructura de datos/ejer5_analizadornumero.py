class AnalizadorNumeros:  
    def __init__(self):  
        self.pares = []  
        self.impares = []  
      
    def es_par(self, numero):  
        return numero % 2 == 0  
      
    def separar(self, *numeros):  
        self.pares.clear()  
        self.impares.clear()  
        for n in numeros:  
            if self.es_par(n):  
                self.pares.append(n)  
            else:  
                self.impares.append(n)  
        return {'pares': self.pares, 'impares': self.impares}  
      
    def cantidad_pares_impares(self):  
        return (len(self.pares), len(self.impares))


# --- Programa principal de prueba ---
analizador = AnalizadorNumeros()

# Probando separación con múltiples argumentos
resultado_separacion = analizador.separar(10, 15, 22, 33, 40)
print(f"Diccionario separado: {resultado_separacion}")

# Consultando conteos en formato de tupla
conteo_total = analizador.cantidad_pares_impares()
print(f"Tupla de conteos (Pares, Impares): {conteo_total}")