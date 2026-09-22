

import math

class MatrizDistancias:  
    def __init__(self, puntos):  
        self.puntos = puntos  # Lista de tuplas [(x1, y1), (x2, y2), ...]
      
    def _calcular_distancia(self, p1, p2):  
        # Fórmula de la distancia euclidiana entre dos puntos
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)  
      
    def generar(self):  
        n = len(self.puntos)  
        # Crear una matriz cuadrada de n x n inicializada en ceros
        matriz = [[0.0] * n for _ in range(n)]  
          
        for i in range(n):  
            for j in range(n):  
                matriz[i][j] = self._calcular_distancia(self.puntos[i], self.puntos[j])  
                  
        return matriz


# --- Programa principal de prueba ---
# Definimos un conjunto de puntos geométricos o cartesianos
puntos_ejemplo = [(0, 0), (3, 4), (1, 1)]

calculador = MatrizDistancias(puntos_ejemplo)
matriz_resultado = calculador.generar()

print(f"Puntos analizados: {puntos_ejemplo}\n")
print("Matriz de distancias resultante:")
for fila in matriz_resultado:
    print([round(val, 2) for val in fila])   