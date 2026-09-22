class ComparadorCursos:
    def __init__(self):
        self.cursos = {}  # {estudiante: {curso, curso, ...}}

    def inscribir(self, estudiante, *cursos):
        if estudiante not in self.cursos:
            self.cursos[estudiante] = set()
        self.cursos[estudiante].update(cursos)

    def cursos_comunes(self, est1, est2):
        return sorted(self.cursos.get(est1, set()) & self.cursos.get(est2, set()))

    def cursos_exclusivos(self, est1, est2):
        return sorted(self.cursos.get(est1, set()) - self.cursos.get(est2, set()))

    def todos_los_cursos(self):
        todos = set()
        for cursos in self.cursos.values():
            todos |= cursos
        return sorted(todos)

cc = ComparadorCursos()
cc.inscribir("Ana", "Python", "BD", "Redes")
cc.inscribir("Luis", "Python", "Web")
print(cc.cursos_comunes("Ana", "Luis"))                   # ['Python']
print(cc.cursos_exclusivos("Ana", "Luis"))                # ['BD', 'Redes']
print(cc.todos_los_cursos())                              # ['BD', 'Python', 'Redes', 'Web']