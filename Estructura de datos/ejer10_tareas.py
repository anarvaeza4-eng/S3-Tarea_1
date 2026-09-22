class Tareas:  
    def __init__(self):  
        self.lista_tareas = []  
      
    def agregar_tarea(self, descripcion, prioridad):  
        self.lista_tareas.append((descripcion, prioridad))  
      
    def tareas_prioritarias(self):  
        return [t for t in self.lista_tareas if t[1].lower() == "alta"]  
      
    def eliminar_completada(self, descripcion):  
        self.lista_tareas = [t for t in self.lista_tareas if t[0] != descripcion]


# --- Programa principal de prueba ---
gestor_tareas = Tareas()

# Agregando tareas con distintas prioridades
gestor_tareas.agregar_tarea("Revisar código del proyecto", "Alta")
gestor_tareas.agregar_tarea("Actualizar documentación", "Media")
gestor_tareas.agregar_tarea("Corregir error crítico en servidor", "ALTA")
gestor_tareas.agregar_tarea("Limpiar escritorio", "Baja")

print(f"Todas las tareas: {gestor_tareas.lista_tareas}")

# Consultando solo las tareas prioritarias
print(f"Tareas prioritarias: {gestor_tareas.tareas_prioritarias()}")

# Eliminando una tarea completada
gestor_tareas.eliminar_completada("Actualizar documentación")
print(f"Tareas después de eliminar 'Actualizar documentación': {gestor_tareas.lista_tareas}")