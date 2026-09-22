class ColaAtencion:
    def __init__(self):
        self.cola = []
        self.atendidos = []

    def llegar(self, nombre):
        self.cola.append(nombre)
        return len(self.cola)

    def llegar_varios(self, *nombres):
        return [self.llegar(n) for n in nombres]

    def atender(self):
        if not self.cola:
            return None
        persona = self.cola.pop(0)
        self.atendidos.append(persona)
        return persona

    def personas_en_espera(self):
        return len(self.cola)

cola = ColaAtencion()
print(cola.llegar("Ana"))                                 # 1
print(cola.llegar_varios("Luis", "Marta"))                # [2, 3]
print(cola.atender())                                     # 'Ana'
print(cola.personas_en_espera())                          # 2
print(cola.atendidos)                                      # ['Ana']