# =====================================================================
#  lista_manual.py  —  LISTA 1: construida DESDE CERO (como MiLista)
# ---------------------------------------------------------------------
#  Por dentro hay un ARREGLO de tamaño fijo con cajones vacíos (None).
#
#      datos     -> [Ana, Beto, Carlos, None, None, ...]
#      capacidad -> cuántos cajones hay en total          (10)
#      cantidad  -> cuántos cajones están ocupados        (3)
#
#  LAS DOS REGLAS QUE EXPLICAN TODA LA CLASE
#    1. Los pasajeros van SEGUIDOS: de datos[0] a datos[cantidad-1].
#       No puede haber huecos (None) en medio.
#    2. Para INSERTAR se corre a la DERECHA (de atrás hacia adelante).
#       Para ELIMINAR se corre a la IZQUIERDA (de adelante hacia atrás).
#
#  En esta clase se trabaja "a mano": solo índices, while, for con
#  range, if, variables auxiliares y los atributos cantidad/capacidad.
#  No se usa ningún método ya hecho de las listas de Python.
# =====================================================================

from pasajero import Pasajero


class ListaPasajerosManual:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad   # los "cajones"
        self.capacidad = capacidad        # cuántos cajones hay
        self.cantidad = 0                 # cuántos están ocupados

    # -----------------------------------------------------------------
    # 1. AÑADIR
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Pone el pasajero en el primer cajón libre (al final)."""
        if self.cantidad == self.capacidad:
            print("⚠ La lista está llena")
            return False
        # Mejora: la cédula es la clave, no se permiten repetidas
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        # El primer cajón libre SIEMPRE es datos[cantidad]
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición."""
        if self.cantidad == 0:
            print("(lista vacía)")
            return
        for i in range(self.cantidad):          # solo los cajones ocupados
            print(f"[{i}] {self.datos[i]}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        """Retorna cuántos pasajeros hay (el dato ya está en self.cantidad)."""
        return self.cantidad

    # -----------------------------------------------------------------
    # 4. INSERTAR EN UNA POSICIÓN
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """Mete el pasajero en 'posicion' corriendo los demás a la DERECHA."""
        if self.cantidad == self.capacidad:
            print("⚠ La lista está llena")
            return False
        # posicion == cantidad SÍ es válida: equivale a añadir al final
        if posicion < 0 or posicion > self.cantidad:
            print("⚠ Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False

        i = self.cantidad                      # empiezo por el último cajón libre
        while i > posicion:
            self.datos[i] = self.datos[i - 1]  # muevo uno a la derecha
            i = i - 1
        # Si se recorriera de adelante hacia atrás se pisarían los datos.

        self.datos[posicion] = pasajero        # el nuevo entra en el hueco
        self.cantidad = self.cantidad + 1
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR (LINEAL) POR CÉDULA
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """Búsqueda lineal. Retorna la POSICIÓN o -1 si no existe."""
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i
        return -1

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA POR CÉDULA
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """
        Búsqueda binaria. REQUISITO: la lista debe estar ordenada por
        cédula (llamar antes a ordenar_asc). Retorna la posición o -1.
        Las cédulas son str; comparar "0901..." < "0912..." funciona
        porque todas tienen 10 dígitos.
        """
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].cedula == cedula:
                return medio
            if self.datos[medio].cedula < cedula:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """Cambia nombre y edad del pasajero con esa cédula."""
        pos = self.buscar(cedula)               # REUTILIZA buscar
        if pos == -1:
            print("⚠ No existe un pasajero con esa cédula")
            return False
        self.datos[pos].nombre = nuevo_nombre
        self.datos[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """Quita el pasajero de esa posición y lo RETORNA (None si no es válida)."""
        if posicion < 0 or posicion >= self.cantidad:
            print("⚠ Posición no válida")
            return None
        valor = self.datos[posicion]            # guardo el que voy a quitar
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]   # corro a la IZQUIERDA
        self.datos[self.cantidad - 1] = None    # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return valor

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """Quita el pasajero que tenga esa cédula, reutilizando dos métodos."""
        pos = self.buscar(cedula)
        if pos == -1:
            print("⚠ No existe un pasajero con esa cédula")
            return False
        self.eliminar_por_posicion(pos)
        return True

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula) — MÉTODO BURBUJA
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """Ordena de menor a mayor cédula."""
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # variable auxiliar
                    self.datos[i + 1] = aux

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """Ordena de MAYOR a menor cédula (solo cambia el símbolo: > pasa a <)."""
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        """Invierte el orden con dos punteros que se acercan."""
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        """Crea OTRA ListaPasajerosManual con los mismos pasajeros."""
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """Retorna una NUEVA lista solo con pasajeros de 18 años o más."""
        resultado = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad():
                resultado.añadir(self.datos[i])
        return resultado

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """Retorna un arreglo con los NOMBRES en mayúsculas."""
        resultado = [None] * self.cantidad      # arreglo del tamaño justo
        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()
        return resultado


# ---------------------------------------------------------------------
#  Prueba rápida: python lista_manual.py
# ---------------------------------------------------------------------
if __name__ == "__main__":
    lista = ListaPasajerosManual()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    print(lista.buscar("0987654321"))   # debe imprimir 2
    lista.listar()
