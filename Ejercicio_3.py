import math 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")
    
    def mover_coordenadas(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia
    
#Definimos los dos puntos
punto1 = Punto(3, 5)
punto1.mostrar_coordenadas()

punto2 = Punto(-2, 7)
punto2.mostrar_coordenadas()

#Cambiamos las coordenadas del punto 1
punto1.mover_coordenadas(1, 2)
punto1.mostrar_coordenadas()

#Calculamos la distancia entre el punto 1 (cambiado) y el punto 2
distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")
    
