class Biblioteca:
    def __init__(self):
        self.libros = {}  # {titulo: disponible (bool)}

    def agregar_libro(self, titulo):
        self.libros[titulo] = True

    def prestar(self, titulo):
        if titulo in self.libros and self.libros[titulo]:
            self.libros[titulo] = False
            return True
        return False

    def prestar_varios(self, *titulos):
        rechazados = []
        for t in titulos:
            if not self.prestar(t):
                rechazados.append(t)
        return rechazados

    def disponibles(self):
        return [t for t, disp in self.libros.items() if disp]
    
        b.agregar_libro("Python")
        b.agregar_libro("Java")
        print(b.prestar("Python"))                              # True
        print(b.prestar_varios("Python", "Java", "C++"))         # ['Python', 'C++']
        print(b.disponibles())                                   # []