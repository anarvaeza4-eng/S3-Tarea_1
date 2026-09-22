class Afinidad:
    def __init__(self):
        self.gustos = {}  # {usuario: {gusto, gusto, ...}}

    def agregar_gustos(self, usuario, *gustos):
        if usuario not in self.gustos:
            self.gustos[usuario] = set()
        self.gustos[usuario].update(gustos)

    def similitud(self, u1, u2):
        g1 = self.gustos.get(u1, set())
        g2 = self.gustos.get(u2, set())
        union = g1 | g2
        if not union:
            return 0.0
        comunes = g1 & g2
        return round(len(comunes) / len(union), 2)

    def mas_afin(self, usuario):
        mejor = None
        mejor_sim = -1
        for otro in self.gustos:
            if otro == usuario:
                continue
            sim = self.similitud(usuario, otro)
            if sim > mejor_sim:
                mejor_sim = sim
                mejor = otro
        return (mejor, mejor_sim)

    def recomendar(self, usuario):
        otro, _ = self.mas_afin(usuario)
        if otro is None:
            return []
        diferencia = self.gustos.get(otro, set()) - self.gustos.get(usuario, set())
        return sorted(diferencia)

af = Afinidad()
af.agregar_gustos("Ana", "rock", "cine", "gym")
af.agregar_gustos("Luis", "rock", "cine", "viajes")
af.agregar_gustos("Marta", "pop", "lectura")
print(af.similitud("Ana", "Luis"))                          # 0.5
print(af.mas_afin("Ana"))                                   # ('Luis', 0.5)
print(af.recomendar("Ana"))                                 # ['viajes']