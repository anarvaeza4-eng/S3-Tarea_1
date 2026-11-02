# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Ejercicios del módulo Listas:
#     • 3 DESARROLLADOS (taller)  -> T1, T2, T3
#     • 5 PROPUESTOS              -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que imprime su
#  enunciado, usa datos fijos y muestra el resultado. Cuando se pide,
#  se resuelve de dos formas:
#     ✋ MANUAL (bucles, patrones del módulo 0)
#     🐍 PYTHON (built-ins y comprensiones)
# =====================================================================

from lista_python import ListaPasajerosPython
from pasajero import Pasajero


# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
    """T1 — CRUD de pasajeros con clase Pasajero + list (Taller, Medio)."""
    print("T1 — CRUD de pasajeros con clase Pasajero + list")
    lista = ListaPasajerosPython()

    print("\n1) Añadir 3 pasajeros")
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))

    print("\n2) Listar")
    lista.listar()

    print("\n3) Buscar por cédula 0912345678")
    pos = lista.buscar("0912345678")
    if pos == -1:
        print("   No existe")
    else:
        print(f"   Encontrado en [{pos}]: {lista.pasajeros[pos]}")

    print("\n4) Modificar 0912345678 -> Anita, 29 años")
    lista.modificar("0912345678", "Anita", 29)
    lista.listar()

    print("\n5) Eliminar la cédula 0987654321 (Luis)")
    lista.eliminar_por_valor("0987654321")
    lista.listar()

    print("\n6) Ordenar por NOMBRE con sort(key=lambda p: p.nombre)")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    lista.listar()


def ejercicio_t2():
    """T2 — Estadísticas de una lista de notas (Taller, Medio)."""
    print("T2 — Estadísticas de una lista de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

    # ✋ MANUAL: un solo for con acumulador, campeón y contador
    suma = 0
    maxima = notas[0]
    minima = notas[0]
    pos_mejor = 0
    aprobados = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
        if notas[i] > maxima:
            maxima = notas[i]
            pos_mejor = i
        if notas[i] < minima:
            minima = notas[i]
        if notas[i] >= 7:
            aprobados = aprobados + 1
    promedio = suma / len(notas)
    print(f"✋ Promedio {promedio:.2f} · Máx {maxima} ({nombres[pos_mejor]}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")

    # 🐍 PYTHON: sum, max, min, len, index y comprensión
    promedio = sum(notas) / len(notas)
    mejor = nombres[notas.index(max(notas))]
    aprobados = len([n for n in notas if n >= 7])
    print(f"🐍 Promedio {promedio:.2f} · Máx {max(notas)} ({mejor}) · "
          f"Mín {min(notas)} · Aprobados {aprobados} de {len(notas)}")


def ejercicio_t3():
    """T3 — Ordenar una lista, bubble sort (Taller, Avanzado)."""
    print("T3 — Ordenar una lista (bubble sort)")
    lista = [5, 2, 8, 1, 9, 3, 7]
    print(f"Original: {lista}")

    # ✋ MANUAL: burbuja con bandera hubo_swap, sobre una COPIA
    copia = lista[:]
    n = len(copia)
    for vuelta in range(n - 1):
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if copia[i] > copia[i + 1]:
                aux = copia[i]
                copia[i] = copia[i + 1]
                copia[i + 1] = aux
                hubo_swap = True
        if not hubo_swap:       # si en una vuelta no hubo cambios, ya está ordenada
            break
    print(f"✋ Burbuja:         {copia}")

    # 🐍 PYTHON: sorted() no modifica; sort() modifica la propia lista
    print(f"🐍 sorted(lista):   {sorted(lista)}")
    descendente = lista[:]
    descendente.sort(reverse=True)
    print(f"🐍 sort(reverse):   {descendente}")

    # Extra: ordenar palabras por longitud con key=len
    palabras = ["python", "a", "código", "el"]
    print(f"Extra key=len:     {sorted(palabras, key=len)}")


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """P1 — Contar apariciones de un valor."""
    print("P1 — Contar apariciones de un valor")
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    # ✋ MANUAL: patrón contador
    contador = 0
    for x in lista:
        if x == v:
            contador = contador + 1
    print(f"✋ {v} aparece {contador} veces")

    # 🐍 PYTHON: count()
    print(f"🐍 {v} aparece {lista.count(v)} veces")

    # 🧩 COMPRENSIÓN
    print(f"🧩 {v} aparece {len([x for x in lista if x == v])} veces")


def ejercicio_p2():
    """P2 — Invertir una lista SIN lista.reverse()."""
    print("P2 — Invertir una lista")
    lista = [1, 2, 3, 4, 5]

    # ✋ MANUAL: for hacia atrás con append
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print(f"✋ {invertida}")

    # 🐍 PYTHON: slicing y reversed()
    print(f"🐍 {lista[::-1]}  |  {list(reversed(lista))}")

    # 🧩 COMPRENSIÓN
    print(f"🧩 {[lista[i] for i in range(len(lista) - 1, -1, -1)]}")


def ejercicio_p3():
    """P3 — Números únicos manteniendo el orden."""
    print("P3 — Números únicos")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    # ✋ MANUAL: recorrer y añadir si no está
    unicos = []
    for n in nums:
        if n not in unicos:
            unicos.append(n)
    print(f"✋ {unicos}")

    # 🐍 PYTHON: dict.fromkeys conserva el orden de inserción
    print(f"🐍 {list(dict.fromkeys(nums))}")
    # list(set(nums)) NO garantiza el orden: un set no guarda orden de
    # inserción, el orden depende del hash de cada elemento.


def ejercicio_p4():
    """P4 — Segundo mayor (sin ordenar toda la lista)."""
    print("P4 — Segundo mayor")
    nums = [5, 2, 9, 7, 9, 3, 8]

    # ✋ MANUAL: dos campeones en un solo recorrido
    mayor = None
    segundo = None
    for n in nums:
        if mayor is None or n > mayor:
            segundo = mayor
            mayor = n
        elif n != mayor and (segundo is None or n > segundo):
            segundo = n
    print(f"✋ Mayor {mayor} · Segundo {segundo}")

    # 🐍 PYTHON (para comprobar)
    ordenados = sorted(set(nums))
    print(f"🐍 Mayor {ordenados[-1]} · Segundo {ordenados[-2]}")


def ejercicio_p5():
    """P5 — Fusionar dos listas ordenadas (sin sort)."""
    print("P5 — Fusionar dos listas ordenadas")
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]

    # ✋ MANUAL: dos índices comparando cabezas (base del merge sort)
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i = i + 1
        else:
            resultado.append(b[j])
            j = j + 1
    resultado.extend(a[i:])     # lo que sobre de a
    resultado.extend(b[j:])     # lo que sobre de b
    print(f"✋ {resultado}")

    # 🐍 PYTHON (para comprobar)
    print(f"🐍 {sorted(a + b)}")


# ============================== CATÁLOGO =============================
#  (código, título, tipo, función)   ->  tipo: "taller" o "propuesto"
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    """Muestra los ejercicios agrupados y ejecuta el elegido hasta escribir 0."""
    # 1. Con COMPRENSIONES se separa el catálogo
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

    while True:
        # 2. Mostrar los dos grupos
        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        print("--- PROPUESTOS ---")
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        print("  0.  Volver")

        # 3. Leer el código y pasarlo a mayúsculas
        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break

        # 4. Buscar la tupla con ese código (otra comprensión)
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]

        # 5. Si existe, llamar a su función
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("  Código no válido")
