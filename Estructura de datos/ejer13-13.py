class Matriz:
    def __init__(self, datos):
        self.datos = datos  # lista de listas

    def suma_filas(self):
        return [sum(fila) for fila in self.datos]

    def suma_columnas(self):
        return [sum(fila[j] for fila in self.datos) for j in range(len(self.datos[0]))]

    def transpuesta(self):
        return [[fila[j] for fila in self.datos] for j in range(len(self.datos[0]))]

    def diagonal_principal(self):
        return tuple(self.datos[i][i] for i in range(len(self.datos)))

m = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m.suma_filas())                                      # [6, 15, 24]
print(m.suma_columnas())                                   # [12, 15, 18]
print(m.transpuesta())                                     # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(m.diagonal_principal())                              # (1, 5, 9)