class ConversorUnidades:
    def __init__(self):
        self.factores = {
            "km_a_millas": 0.621371,
            "kg_a_libras": 2.20462,
            "m_a_pies": 3.28084,
        }

    def convertir(self, valor, tipo):
        if tipo not in self.factores:
            return None
        return round(valor * self.factores[tipo], 2)

    def convertir_lote(self, tipo, *valores):
        return [self.convertir(v, tipo) for v in valores]

    def agregar_factor(self, tipo, factor):
        self.factores[tipo] = factor

        cu = ConversorUnidades()
        print(cu.convertir(10, "km_a_millas"))                    # 6.21
        print(cu.convertir_lote("kg_a_libras", 1, 5, 10))         # [2.2, 11.02, 22.05]
        print(cu.convertir(5, "litros_a_galones"))                # None