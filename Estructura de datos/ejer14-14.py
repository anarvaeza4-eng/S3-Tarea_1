class Ranking:
    def __init__(self):
        self.jugadores = {}  # {jugador: [puntajes]}

    def registrar(self, jugador, puntaje):
        if jugador not in self.jugadores:
            self.jugadores[jugador] = []
        self.jugadores[jugador].append(puntaje)

    def registrar_varios(self, jugador, *puntajes):
        for p in puntajes:
            self.registrar(jugador, p)

    def mejor_puntaje(self, jugador):
        return max(self.jugadores.get(jugador, [0]))

    def top(self, n):
        mejores = [(j, max(p)) for j, p in self.jugadores.items()]
        mejores.sort(key=lambda x: x[1], reverse=True)
        return mejores[:n]

r = Ranking()
r.registrar_varios("Ana", 120, 300, 250)
r.registrar_varios("Luis", 400, 90)
r.registrar("Marta", 310)
print(r.mejor_puntaje("Ana"))                              # 300
print(r.top(2))                                             # [('Luis', 400), ('Marta', 310)]