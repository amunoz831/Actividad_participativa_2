class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Kilometraje: {self.kilometraje} km")

vehiculo1 = Vehiculo(200, 50000)
vehiculo1.mostrar_informacion()