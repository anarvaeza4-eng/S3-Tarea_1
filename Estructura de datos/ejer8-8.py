class ValidadorClave:
    def __init__(self):
        self.claves_aceptadas = []

    def errores(self, clave):
        errs = []
        if len(clave) < 8:
            errs.append("longitud")
        if not any(c.isupper() for c in clave):
            errs.append("mayuscula")
        if not any(c.isdigit() for c in clave):
            errs.append("digito")
        if not any(c in "!@#$%&*" for c in clave):
            errs.append("simbolo")
        return errs

    def es_valida(self, clave):
        errs = self.errores(clave)
        if not errs:
            self.claves_aceptadas.append(clave)
            return True
        return False

    def validar_lote(self, *claves):
        return {c: self.errores(c) for c in claves}

v = ValidadorClave()
print(v.errores("hola"))                                  # ['longitud', 'mayuscula', 'digito', 'simbolo']
print(v.es_valida("Segura#2026"))                         # True
print(v.validar_lote("abc", "Ab1#xyz9"))
    # {'abc': ['longitud', 'mayuscula', 'digito', 'simbolo'], 'Ab1#xyz9': []}
print(v.claves_aceptadas)                                 # ['Segura#2026']