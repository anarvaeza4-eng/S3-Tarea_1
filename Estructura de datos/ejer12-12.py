class GeneradorSecuencias:
    def fibonacci(self, n):
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return tuple(secuencia)

    def cuadrados(self, n):
        return tuple(i * i for i in range(1, n + 1))

    def triangulares(self, n):
        secuencia = []
        total = 0
        for i in range(1, n + 1):
            total += i
            secuencia.append(total)
        return tuple(secuencia)

    def generar(self, tipo, n):
        metodos = {
            "fibonacci": self.fibonacci,
            "cuadrados": self.cuadrados,
            "triangulares": self.triangulares,
        }
        if tipo not in metodos:
            return ()
        return metodos[tipo](n)

    def generar_lote(self, n, *tipos):
        return {tipo: self.generar(tipo, n) for tipo in tipos}

g = GeneradorSecuencias()
print(g.fibonacci(7))                                      # (0, 1, 1, 2, 3, 5, 8)
print(g.generar("triangulares", 5))                        # (1, 3, 6, 10, 15)
print(g.generar_lote(4, "cuadrados", "fibonacci"))
    # {'cuadrados': (1, 4, 9, 16), 'fibonacci': (0, 1, 1, 2)}
print(g.generar("primos", 3))                              # ()