import random

class GestorEquipos:  
    def __init__(self):  
        self.equipos = {}  
      
    def formar_equipos(self, num_equipos, *participantes):  
        if num_equipos <= 0:  
            raise ValueError("El número de equipos debe ser mayor a cero.")  
          
        # Convertir los argumentos en lista y mezclarlos aleatoriamente  
        lista_participantes = list(participantes)  
        random.shuffle(lista_participantes)  
          
        # Inicializar los diccionarios para cada equipo  
        self.equipos = {f"Equipo {i+1}": [] for i in range(num_equipos)}  
          
        # Distribuir equitativamente de forma cíclica  
        for indice, participante in enumerate(lista_participantes):  
            nombre_equipo = f"Equipo {(indice % num_equipos) + 1}"  
            self.equipos[nombre_equipo].append(participante)  
              
        return self.equipos


# --- Programa principal de prueba ---
gestor = GestorEquipos()

# Definiendo participantes por lotes y solicitando 3 equipos
resultado_equipos = gestor.formar_equipos(
    3, "Mateo", "Valentina", "Santiago", "Camila", "Alejandro", "Valeria", "Lucas"
)

print("--- Distribución de Equipos ---")
for equipo, integrantes in resultado_equipos.items():
    print(f"{equipo}: {integrantes}")