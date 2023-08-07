class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

propietarios = ["Juan Pérez", "María Gómez"]
cuenta1 = CuentaBancaria("123456789", propietarios, 5000.0)

print(f"Número de cuenta: {cuenta1.numero_cuenta}")
print(f"Propietarios: {', '.join(cuenta1.propietarios)}")
print(f"Balance: {cuenta1.balance}")