class Urna:
    def __init__(self, candidatos):
        self.votos = {c: 0 for c in candidatos}

    def votar(self, candidato):
        if candidato not in self.votos:
            return False
        self.votos[candidato] += 1
        return True

    def votar_varios(self, *candidatos):
        invalidos = 0
        for c in candidatos:
            if not self.votar(c):
                invalidos += 1
        return invalidos

    def ganadores(self):
        maximo = max(self.votos.values())
        return [c for c, v in self.votos.items() if v == maximo]

    def porcentajes(self):
        total = sum(self.votos.values())
        if total == 0:
            return {c: 0.0 for c in self.votos}
        return {c: round(v / total * 100, 1) for c, v in self.votos.items()}
u = Urna(["Ana", "Luis", "Marta"])
print(u.votar_varios("Ana", "Luis", "Ana", "Zoe", "Marta", "Ana"))  # 1
print(u.ganadores())                                        # ['Ana']
print(u.porcentajes())                                      # {'Ana': 60.0, 'Luis': 20.0, 'Marta': 20.0}