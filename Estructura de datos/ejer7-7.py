class Agenda:
    def __init__(self):
        self.contactos = {}  # {nombre: (telefono, correo)}

    def agregar(self, nombre, telefono, correo):
        self.contactos[nombre] = (telefono, correo)

    def buscar_prefijo(self, prefijo):
        prefijo = prefijo.lower()
        return [n for n in self.contactos if n.lower().startswith(prefijo)]

    def telefono_de(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre][0]
        return "No existe"

    def eliminar(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return True
        return False

ag = Agenda()
ag.agregar("Carlos", "0991111111", "carlos@mail.com")
ag.agregar("Camila", "0982222222", "cami@mail.com")
ag.agregar("Luis", "0973333333", "luis@mail.com")
print(ag.buscar_prefijo("ca"))                            # ['Carlos', 'Camila']
print(ag.telefono_de("Luis"))                             # '0973333333'
print(ag.eliminar("Luis"))                                # True
print(ag.telefono_de("Luis"))                             # 'No existe'