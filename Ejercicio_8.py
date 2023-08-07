class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad>0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad} a la cuenta.")
        else:
            print("La cantidad a depositar tiene que ser mayor que 0")

propietarios = ["Juan Pérez", "María Gómez"]
cuenta1 = CuentaBancaria("123456789", propietarios, 5000.0)

print(f"Número de cuenta: {cuenta1.numero_cuenta}")
print(f"Propietarios: {', '.join(cuenta1.propietarios)}")
print(f"Balance: {cuenta1.balance}")

cuenta1.depositar(1500.0)
print(f"Nuevo balance: {cuenta1.balance}")