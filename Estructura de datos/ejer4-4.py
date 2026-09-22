class Parqueadero:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = {}  # {placa: hora_entrada}
        self.tarifa_hora = 1.5

    def ingresar(self, placa, hora):
        if len(self.vehiculos) >= self.capacidad or placa in self.vehiculos:
            return False
        self.vehiculos[placa] = hora
        return True

    def ingresar_varios(self, *vehiculos):
        rechazados = []
        for placa, hora in vehiculos:
            if not self.ingresar(placa, hora):
                rechazados.append(placa)
        return rechazados

    def salir(self, placa, hora_salida):
        if placa not in self.vehiculos:
            return None
        hora_entrada = self.vehiculos.pop(placa)
        horas = max(1, hora_salida - hora_entrada)
        return horas * self.tarifa_hora

    def espacios_libres(self):
        return self.capacidad - len(self.vehiculos)

p = Parqueadero(2)
print(p.ingresar_varios(("ABC-123", 8), ("XYZ-999", 9), ("DEF-456", 10)))  # ['DEF-456']
print(p.espacios_libres())                                # 0
print(p.salir("ABC-123", 12))                             # 6.0
print(p.espacios_libres())                                # 1