class CompresorRLE:
    def comprimir(self, texto):
        if not texto:
            return []
        pares = []
        actual = texto[0]
        contador = 1
        for c in texto[1:]:
            if c == actual:
                contador += 1
            else:
                pares.append((actual, contador))
                actual = c
                contador = 1
        pares.append((actual, contador))
        return pares

    def descomprimir(self, pares):
        return "".join(c * n for c, n in pares)

    def a_cadena(self, pares):
        return "".join(f"{c}{n}" for c, n in pares)

    def tasa_compresion(self, texto):
        compacto = self.a_cadena(self.comprimir(texto))
        return round(len(compacto) / len(texto), 2)
    
cr = CompresorRLE()
print(cr.comprimir("aaaabbbccd"))                           # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print(cr.descomprimir([("x", 3), ("y", 2)]))                # 'xxxyy'
print(cr.a_cadena(cr.comprimir("aaaabbbccd")))              # 'a4b3c2d1'
print(cr.tasa_compresion("aaaabbbccd"))                     # 0.8