class CuentaAhorros:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # [(tipo, monto)]

    def depositar(self, monto):
        if monto <= 0:
            return False
        self.saldo += monto
        self.movimientos.append(("deposito", monto))
        return True

    def retirar(self, monto):
        if monto <= 0 or monto > self.saldo:
            return False
        self.saldo -= monto
        self.movimientos.append(("retiro", monto))
        return True

    def resumen(self):
        depositos = sum(m for tipo, m in self.movimientos if tipo == "deposito")
        retiros = sum(m for tipo, m in self.movimientos if tipo == "retiro")
        return {"depositos": depositos, "retiros": retiros, "saldo": self.saldo}

c = CuentaAhorros("Ana", 100)
print(c.depositar(50))                                    # True
print(c.retirar(300))                                     # False
print(c.retirar(30))                                      # True
print(c.resumen())                                         # {'depositos': 50, 'retiros': 30, 'saldo': 120}