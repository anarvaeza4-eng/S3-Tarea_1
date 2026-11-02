# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero usando lo que Python ya
#  trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  Comprensiones usadas en: buscar, buscar_binaria, eliminar_por_valor,
#  filtrar_mayores_de_edad y nombres_en_mayusculas.
#
#  Sintaxis:
#       [EXPRESIÓN for ELEMENTO in LISTA]            -> transformar
#       [ELEMENTO  for ELEMENTO in LISTA if COND]    -> filtrar
# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Añade al final con append(), sin permitir cédulas repetidas."""
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.append(pasajero)
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        """Retorna cuántos pasajeros hay con len()."""
        return len(self.pasajeros)

    # -----------------------------------------------------------------
    # 4. INSERTAR
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """
        Usa insert(). Valida 0 <= posicion <= len(...) (posicion == len
        equivale a añadir al final).

        PIENSA: ¿Python corre los elementos o no?
        RESPUESTA: sí los corre. insert() mueve hacia la derecha todos los
        elementos desde 'posicion' hasta el final, igual que el while de la
        Lista 1, solo que lo hace internamente en C. Por eso NO es gratis:
        su complejidad es O(n) en el peor caso (insertar al inicio) y O(1)
        solo si se inserta al final.
        """
        if posicion < 0 or posicion > len(self.pasajeros):
            print("⚠ Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (con COMPRENSIÓN)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """Retorna la posición (int) o -1, juntando coincidencias con una comprensión."""
        posiciones = [i for i, p in enumerate(self.pasajeros)
                      if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

        # EXTRA, versión con next() (se detiene en la primera coincidencia):
        # return next((i for i, p in enumerate(self.pasajeros)
        #              if p.cedula == cedula), -1)

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (con COMPRENSIÓN + bisect)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """
        REQUISITO: lista ordenada por cédula (ordenar_asc antes).
        Retorna la posición o -1.
        """
        cedulas = [p.cedula for p in self.pasajeros]      # COMPRENSIÓN
        i = bisect_left(cedulas, cedula)                  # dónde "debería" estar
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """Cambia nombre y edad del pasajero con esa cédula."""
        pos = self.buscar(cedula)
        if pos == -1:
            print("⚠ No existe un pasajero con esa cédula")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """Usa pop(posicion), que retorna el eliminado (None si no es válida)."""
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("⚠ Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — dos formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """
        FORMA 1 (remove) — queda comentada para comparar:
            pos = self.buscar(cedula)
            if pos == -1:
                print("⚠ No existe un pasajero con esa cédula")
                return False
            self.pasajeros.remove(self.pasajeros[pos])
            return True

        FORMA 2 (COMPRENSIÓN) — la que está activa.
        """
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        eliminado = len(self.pasajeros) < antes      # True si eliminó algo
        if not eliminado:
            print("⚠ No existe un pasajero con esa cédula")
        return eliminado

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """
        Usa sort(key=lambda p: p.cedula).

        PIENSA: ¿qué hace key=? ¿qué error sale si lo quitas?
        RESPUESTA: key= es una función que sort() aplica a CADA elemento para
        obtener el valor por el que va a comparar; aquí, de cada Pasajero
        saca su cédula. Sin key, Python intenta comparar los objetos Pasajero
        directamente con "<" y, como la clase no define cómo compararlos,
        lanza: TypeError: '<' not supported between instances of 'Pasajero'
        and 'Pasajero'.
        """
        self.pasajeros.sort(key=lambda p: p.cedula)

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """Usa sort(key=..., reverse=True)."""
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        """Usa reverse(): invierte el orden actual (no es lo mismo que ordenar_desc)."""
        self.pasajeros.reverse()

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        """
        Crea otra lista con copy().

        PIENSA: reversa la copia, luego modifica un pasajero de la copia y
        lista el original. ¿Qué pasó y por qué?
        RESPUESTA: al reversar la copia, el ORIGINAL no cambia de orden,
        porque son dos listas distintas. Pero al modificar un pasajero de la
        copia, el original SÍ cambia, porque es una copia SUPERFICIAL: copy()
        duplica la lista, no los objetos Pasajero de adentro. Las dos listas
        apuntan a los MISMOS objetos. Para evitarlo habría que usar
        copy.deepcopy.
        """
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """Retorna una NUEVA ListaPasajerosPython solo con mayores de edad."""
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """Retorna una list de str con los nombres en mayúsculas."""
        return [p.nombre.upper() for p in self.pasajeros]


# ---------------------------------------------------------------------
#  Prueba rápida: python lista_python.py
# ---------------------------------------------------------------------
if __name__ == "__main__":
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    print(lista.buscar("0987654321"))   # debe imprimir 2
    lista.listar()
