class CuentaBancaria:
    PORCENTAJE_CUOTA_MANEJO = 0.02

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

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta")
        else:
            print("No hay saldo suficiente para realizar el retiro.")
    
    def aplicar_cuota_manejo(self):
        cuota=self.balance * CuentaBancaria.PORCENTAJE_CUOTA_MANEJO
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo de {cuota} a la cuenta.")


propietarios = ["Juan Pérez", "María Gómez"]
cuenta1 = CuentaBancaria("123456789", propietarios, 5000.0)

print(f"Número de cuenta: {cuenta1.numero_cuenta}")
print(f"Propietarios: {', '.join(cuenta1.propietarios)}")
print(f"Balance: {cuenta1.balance}")

cuenta1.depositar(1500.0)
print(f"Nuevo balance: {cuenta1.balance}")

cuenta1.retirar(2000.0)
print(f"Nuevo balance: {cuenta1.balance}")

cuenta1.aplicar_cuota_manejo()
print(f"Nuevo balance después de la cuota de manejo: {cuenta1.balance}")