class GestorPersonas:  
    def __init__(self):  
        self.personas = {}  
      
    def agregar_persona(self, nombre, edad):  
        self.personas[nombre] = edad  
      
    def personas_mayores(self, edad_minima):  
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]  
      
    def edad_promedio(self):  
        if not self.personas:  
            return 0.0  
        return sum(self.personas.values()) / len(self.personas)


# --- Programa principal de prueba ---
gp = GestorPersonas()

# Agregando personas al diccionario
gp.agregar_persona("Sofía", 22)
gp.agregar_persona("Mateo", 15)
gp.agregar_persona("Lucía", 30)
gp.agregar_persona("Diego", 45)

print(f"Diccionario de personas: {gp.personas}")

# Filtrando personas con edad mayor o igual a 21
umbral = 21
print(f"Personas con edad >= {umbral}: {gp.personas_mayores(umbral)}")

# Calculando promedio de edades
print(f"Edad promedio general: {gp.edad_promedio():.1f} años")