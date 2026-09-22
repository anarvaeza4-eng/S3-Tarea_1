class Asistencia:
    def __init__(self, matriculados):
        self.matriculados = set(matriculados)
        self.presentes = set()

    def marcar_presente(self, nombre):
        if nombre in self.matriculados:
            self.presentes.add(nombre)
            return True
        return False

    def marcar_varios(self, *nombres):
        no_matriculados = []
        for n in nombres:
            if not self.marcar_presente(n):
                no_matriculados.append(n)
        return no_matriculados

    def ausentes(self):
        return sorted(self.matriculados - self.presentes)

    def porcentaje_asistencia(self):
        if not self.matriculados:
            return 0.0
        return round(len(self.presentes) / len(self.matriculados) * 100, 2)

a3 = Asistencia(["Ana", "Luis", "Marta", "Pedro"])
print(a3.marcar_presente("Ana"))                          # True
print(a3.marcar_varios("Luis", "Zoe", "Ana"))             # ['Zoe']
print(a3.ausentes())                                      # ['Marta', 'Pedro']
print(a3.porcentaje_asistencia())                         # 50.0