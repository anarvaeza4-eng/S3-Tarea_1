class GestorTemperatura:  
    def __init__(self):  
        self.temperaturas = []  
      
    def registrar_temperatura(self, temp):  
        self.temperaturas.append(temp)  
      
    def registrar_multiples(self, *temps):  
        for t in temps:  
            self.registrar_temperatura(t)  
              
    def minima(self):  
        return min(self.temperaturas) if self.temperaturas else 0  
          
    def maxima(self):  
        return max(self.temperaturas) if self.temperaturas else 0  
          
    def promedio(self):  
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else 0


# --- Programa principal de prueba ---
gestor = GestorTemperatura()

# Registrando temperaturas individuales y múltiples
gestor.registrar_temperatura(21.5)
gestor.registrar_multiples(19.0, 28.4, 24.1, 22.0)

print(f"Lista de temperaturas: {gestor.temperaturas}")
print(f"Temperatura mínima: {gestor.minima()} °C")
print(f"Temperatura máxima: {gestor.maxima()} °C")
print(f"Temperatura promedio: {gestor.promedio():.2f} °C")