import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, punto_esquina_sup_izq, punto_esquina_inf_der):
        self.esquina_sup_izq = punto_esquina_sup_izq
        self.esquina_inf_der = punto_esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura


punto_sup_izq = Punto(1, 5)
punto_inf_der = Punto(6, 2)

rectangulo1 = Rectangulo(punto_sup_izq, punto_inf_der)

print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")

if rectangulo1.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")








