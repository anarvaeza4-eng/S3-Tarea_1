class LimpiadorDatos:
    def quitar_duplicados(self, datos):
        vistos = set()
        resultado = []
        for d in datos:
            if d not in vistos:
                vistos.add(d)
                resultado.append(d)
        return resultado

    def quitar_invalidos(self, datos):
        return [d for d in datos if d is not None and d >= 0]

    def limpiar(self, datos):
        return self.quitar_duplicados(self.quitar_invalidos(datos))

    def reporte(self, datos):
        limpio = self.limpiar(datos)
        return (len(datos), len(limpio), len(datos) - len(limpio))

lim = LimpiadorDatos()
print(lim.quitar_duplicados([3, 1, 3, 2, 1]))               # [3, 1, 2]
print(lim.quitar_invalidos([4, None, -2, 7, 0]))            # [4, 7, 0]
print(lim.limpiar([5, None, 5, -1, 8, 8, 2]))               # [5, 8, 2]
print(lim.reporte([5, None, 5, -1, 8, 8, 2]))               # (7, 3, 4)