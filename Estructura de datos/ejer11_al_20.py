#----contador de frecuencia---
class ContadorFrecuencia:  
    def __init__(self):  
        self.frecuencias = {}  
        self.mas_frecuente = None  
      
    def analizar(self, texto):  
        palabras = texto.lower().split()  
        self.frecuencias.clear()  
          
        for p in palabras:  
            self.frecuencias[p] = self.frecuencias.get(p, 0) + 1  
              
        if self.frecuencias:  
            self.mas_frecuente = max(self.frecuencias, key=self.frecuencias.get)  
              
        return self.frecuencias

# --- Programa principal de prueba ---
cf = ContadorFrecuencia()

texto_prueba = "manzana pera manzana naranja pera manzana"
resultado = cf.analizar(texto_prueba)

print(f"Texto analizado: '{texto_prueba}'")
print(f"Diccionario de frecuencias: {resultado}")
print(f"Elemento más frecuente: '{cf.mas_frecuente}'")

# --- Programa principal de prueba 12 ---
cf = ContadorFrecuencia()

texto_prueba = "manzana pera manzana naranja pera manzana"
resultado = cf.analizar(texto_prueba)

print(f"Texto analizado: '{texto_prueba}'")
print(f"Diccionario de frecuencias: {resultado}")
print(f"Elemento más frecuente: '{cf.mas_frecuente}'")

#----Selector de rango con tuplas----
class SelectorRango:  
    def __init__(self, *elementos):  
        self.datos = list(elementos)  
      
    def agregar(self, elemento):  
        self.datos.append(elemento)  
      
    def filtrar(self, rango):  
        # Desempaquetamos la tupla (minimo, maximo)  
        min_val, max_val = rango  
        
        # Filtramos usando comprensión de listas dentro del rango inclusivo  
        return [x for x in self.datos if min_val <= x <= max_val]


# --- Programa principal de prueba ---
selector = SelectorRango(8, 15, 22, 35, 42, 10, 50)

print(f"Colección completa de elementos: {selector.datos}")

# Definimos el rango como una tupla (mínimo, máximo)
rango_busqueda = (10, 40)
resultados_filtrados = selector.filtrar(rango_busqueda)

print(f"Elementos dentro del rango {rango_busqueda}: {resultados_filtrados}")

#---Combinador de listas---
class CombinadorListas:
    def __init__(self):
        pass
      
    def intercalar(self, lista1, lista2):
        """Intercala los elementos de ambas listas de forma alternada: [a1, b1, a2, b2, ...]"""
        resultado = []
        for x, y in zip(lista1, lista2):
            resultado.append(x)
            resultado.append(y)
            
        # Añadir los elementos restantes de la lista que sea más larga
        if len(lista1) > len(lista2):
            resultado.extend(lista1[len(lista2):])
        else:
            resultado.extend(lista2[len(lista1):])
            
        return resultado
      
    def emparejar(self, lista1, lista2):
        """Combina ambas listas en una lista de tuplas: [(a1, b1), (a2, b2), ...]"""
        return list(zip(lista1, lista2))


# --- Programa principal de prueba 13 ---
combinador = CombinadorListas()

numeros = [10, 20, 30, 40, 50]
letras = ['x', 'y', 'z']

print(f"Lista 1: {numeros}")
print(f"Lista 2: {letras}")

# Probando entrelazado alternado
resultado_intercalado = combinador.intercalar(numeros, letras)
print(f"Resultado intercalado: {resultado_intercalado}")

# Probando emparejamiento con tuplas
resultado_emparejado = combinador.emparejar(numeros, letras)
print(f"Resultado emparejado (tuplas): {resultado_emparejado}")

#---Mapeo de estudiantes a notas---
class MapeoEstudiantes:  
    def __init__(self):  
        self.registros = {}  
      
    def agregar_estudiante(self, nombre, notas):  
        self.registros[nombre] = notas  
      
    def promedio_estudiante(self, nombre):  
        if nombre not in self.registros or not self.registros[nombre]:  
            return 0.0  
        notas = self.registros[nombre]  
        return sum(notas) / len(notas)  
      
    def estudiantes_aprobados(self, nota_minima):  
        aprobados = []  
        for nombre in self.registros:  
            promedio = self.promedio_estudiante(nombre)  
            if promedio >= nota_minima:  
                aprobados.append(nombre)  
        return aprobados


# --- Programa principal de prueba 14 ---
sistema = MapeoEstudiantes()

# Agregando estudiantes y sus listas de notas
sistema.agregar_estudiante("Mateo", [88, 92, 79])
sistema.agregar_estudiante("Valentina", [55, 62, 70])
sistema.agregar_estudiante("Alejandro", [91, 95, 89])
sistema.agregar_estudiante("Camila", [70, 75, 80])

print(f"Registros de estudiantes: {sistema.registros}")

# Consultando el promedio de un estudiante específico
alumno = "Mateo"
print(f"Promedio de {alumno}: {sistema.promedio_estudiante(alumno):.2f}")

# Filtrando estudiantes aprobados con un umbral de 75
umbral = 75
print(f"Estudiantes aprobados (promedio >= {umbral}): {sistema.estudiantes_aprobados(umbral)}")

#--- Divisores de un número 15 ---
class AnalizadorDivisores:  
    def __init__(self, numero):  
        if numero <= 0:  
            raise ValueError("El número debe ser un entero positivo.")  
        self.numero = numero  
      
    def obtener_divisores(self):  
        return [i for i in range(1, self.numero + 1) if self.numero % i == 0]  
      
    def es_primo(self):  
        divisores = self.obtener_divisores()  
        # Un número primo tiene exactamente dos divisores: 1 y sí mismo  
        return len(divisores) == 2


# --- Programa principal de prueba ---
analizador = AnalizadorDivisores(36)

print(f"Número analizado: {analizador.numero}")
print(f"Divisores: {analizador.obtener_divisores()}")
print(f"¿Es primo?: {analizador.es_primo()}")

print("-" * 30)

# Probando con un número primo
analizador_primo = AnalizadorDivisores(13)
print(f"Número analizado: {analizador_primo.numero}")
print(f"Divisores: {analizador_primo.obtener_divisores()}")
print(f"¿Es primo?: {analizador_primo.es_primo()}")

#---Codificador/Decodificador 16 ---
class CodificadorCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento

    def _desplazar_caracter(self, caracter, shift):
        if not caracter.isalpha():
            return caracter  # Mantener espacios, números y símbolos intactos
        
        # Determinar si es mayúscula o minúscula
        base = ord('A') if caracter.isupper() else ord('a')
        
        # Aplicar el desplazamiento circular con módulo 26
        codigo_original = ord(caracter) - base
        nuevo_codigo = (codigo_original + shift) % 26
        
        return chr(base + nuevo_codigo)

    def codificar(self, mensaje):
        return "".join([self._desplazar_caracter(c, self.desplazamiento) for c in mensaje])

    def decodificar(self, mensaje):
        return "".join([self._desplazar_caracter(c, -self.desplazamiento) for c in mensaje])


# --- Programa principal de prueba ---
codec = CodificadorCesar(desplazamiento=4)

mensaje_original = "Programar en Python es genial 2026!"
mensaje_cifrado = codec.codificar(mensaje_original)
mensaje_descifrado = codec.decodificar(mensaje_cifrado)

print(f"Mensaje original:  '{mensaje_original}'")
print(f"Mensaje cifrado:   '{mensaje_cifrado}'")
print(f"Mensaje descifrado:'{mensaje_descifrado}'")

#---Grupo de edades 17 ---
class ClasificadorEdades:  
    def __init__(self, *edades):  
        self.edades = list(edades)  
      
    def agregar_edad(self, edad):  
        self.edades.append(edad)  
      
    def generar_reporte(self):  
        reporte = {
            "Niños": 0, 
            "Jóvenes": 0, 
            "Adultos": 0, 
            "Adultos Mayores": 0
        }  
          
        for edad in self.edades:  
            if edad < 0:
                raise ValueError(f"Edad no válida encontrada: {edad}")
            elif edad <= 12:  
                reporte["Niños"] += 1  
            elif edad <= 25:  
                reporte["Jóvenes"] += 1  
            elif edad <= 59:  
                reporte["Adultos"] += 1  
            else:  
                reporte["Adultos Mayores"] += 1  
                  
        return reporte


# --- Programa principal de prueba ---
# Registrando un grupo diverso de edades
grupo = ClasificadorEdades(5, 14, 19, 32, 45, 62, 70, 8, 22)

print(f"Edades registradas: {grupo.edades}")

# Generando y mostrando el reporte demográfico
resumen_demografico = grupo.generar_reporte()
print("\n--- Reporte Demográfico ---")
for categoria, cantidad in resumen_demografico.items():
    print(f"{categoria}: {cantidad} persona(s)")

 