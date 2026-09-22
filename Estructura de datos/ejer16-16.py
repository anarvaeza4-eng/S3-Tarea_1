class ConversorBinario:
    def __init__(self):
        self.historial = {}  # {numero: binario}

    def a_binario(self, n):
        if n == 0:
            self.historial[n] = "0"
            return "0"
        binario = ""
        num = n
        while num > 0:
            binario = str(num % 2) + binario
            num //= 2
        self.historial[n] = binario
        return binario

    def a_decimal(self, binario):
        decimal = 0
        for digito in binario:
            decimal = decimal * 2 + int(digito)
        return decimal

    def contar_unos(self, n):
        binario = self.a_binario(n)
        return binario.count("1")

    def convertir_varios(self, *numeros):
        return {n: self.a_binario(n) for n in numeros}

cb = ConversorBinario()
print(cb.a_binario(10))                                     # '1010'
print(cb.a_decimal("1101"))                                 # 13
print(cb.contar_unos(255))                                  # 8
print(cb.convertir_varios(1, 2, 5))                         # {1: '1', 2: '10', 5: '101'}    