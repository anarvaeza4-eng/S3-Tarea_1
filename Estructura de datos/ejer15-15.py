class SalaReuniones:
    def __init__(self, salas):
        self.salas = {sala: set() for sala in salas}  # {sala: {horas ocupadas}}

    def reservar(self, sala, hora):
        if sala not in self.salas:
            return False
        if hora < 0 or hora > 23:
            return False
        if hora in self.salas[sala]:
            return False
        self.salas[sala].add(hora)
        return True

    def reservar_varias(self, sala, *horas):
        rechazadas = []
        for h in horas:
            if not self.reservar(sala, h):
                rechazadas.append(h)
        return rechazadas

    def horas_libres(self, sala, inicio, fin):
        ocupadas = self.salas.get(sala, set())
        return [h for h in range(inicio, fin + 1) if h not in ocupadas]

    def sala_mas_ocupada(self):
        return max(self.salas, key=lambda s: len(self.salas[s]))

s = SalaReuniones(["A", "B"])
print(s.reservar("A", 9))                                  # True
print(s.reservar_varias("A", 9, 10, 11))                   # [9]
print(s.horas_libres("A", 8, 12))                          # [8, 12]
print(s.sala_mas_ocupada())                                # 'A'