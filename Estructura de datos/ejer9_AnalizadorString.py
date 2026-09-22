class AnalizadorString:  
    def __init__(self):  
        self.texto_mas_largo = ""  
      
    def solo_vocales(self, letra):  
        return letra.lower() in "aeiouáéíóú"  
      
    def contar_por_tipo(self, texto):  
        if len(texto) > len(self.texto_mas_largo):  
            self.texto_mas_largo = texto  
            
        res = {'vocales': 0, 'consonantes': 0, 'digitos': 0}  
        
        for c in texto:  
            if c.isdigit():  
                res['digitos'] += 1  
            elif c.isalpha():  
                if self.solo_vocales(c):  
                    res['vocales'] += 1  
                else:  
                    res['consonantes'] += 1  
                    
        return res


# --- Programa principal de prueba ---
analizador = AnalizadorString()

# Analizando cadenas de texto
texto_prueba = "Programacion 2026"
resultado = analizador.contar_por_tipo(texto_prueba)

print(f"Texto analizado: '{texto_prueba}'")
print(f"Conteo clasificado: {resultado}")
print(f"Texto más largo registrado hasta ahora: '{analizador.texto_mas_largo}'")