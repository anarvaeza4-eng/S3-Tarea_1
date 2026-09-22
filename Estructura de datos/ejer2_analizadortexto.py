class AnalizadorTexto:

    def __init__(self):
        # Lista para mantener el orden de todas las palabras ingresadas
        self.lista_palabras = []
        # Conjunto para almacenar únicamente palabras únicas (sin duplicados)
        self.conjunto_unicas = set()
    
    def agregar_palabra(self, palabra):
        """Agrega una palabra a la lista y al conjunto."""
        self.lista_palabras.append(palabra)
        self.conjunto_unicas.add(palabra)
    
    def agregar_multiples(self, *args):
        """Reutiliza agregar_palabra para procesar múltiples palabras a la vez."""
        for palabra in args:
            self.agregar_palabra(palabra)
            
    def contar_palabras(self):
        """Retorna la cantidad de palabras únicas encontradas."""
        return len(self.conjunto_unicas)


at = AnalizadorTexto()

# Agregando palabras en lote (con repeticiones)
at.agregar_multiples("hola", "mundo", "hola", "python", "mundo")

# Ver resultados
print(f"Secuencia completa en orden: {at.lista_palabras}")
print(f"Palabras únicas guardadas: {at.conjunto_unicas}")
print(f"Cantidad de palabras únicas: {at.contar_palabras()}")
    