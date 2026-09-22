class JuegoPalabras:
    def es_palindromo(self, texto):
        limpio = texto.replace(" ", "").lower()
        return limpio == limpio[::-1]

    def son_anagramas(self, a, b):
        return sorted(a.lower()) == sorted(b.lower())

    def filtrar_palindromos(self, *textos):
        return [t for t in textos if self.es_palindromo(t)]

    def grupos_anagramas(self, *palabras):
        grupos = {}
        for p in palabras:
            clave = "".join(sorted(p.lower()))
            grupos.setdefault(clave, []).append(p)
        return {clave: lista for clave, lista in grupos.items() if len(lista) >= 2}

jp = JuegoPalabras()
print(jp.es_palindromo("Anita lava la tina"))             # True
print(jp.son_anagramas("roma", "amor"))                   # True
print(jp.filtrar_palindromos("oso", "casa", "Ana", "radar"))  # ['oso', 'Ana', 'radar']
print(jp.grupos_anagramas("roma", "amor", "ramo", "sol", "los", "mesa"))
    # {'amor': ['roma', 'amor', 'ramo'], 'los': ['sol', 'los']}