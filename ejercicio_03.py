"""El ejercicio exige conservar imprimir_informe() sin modificaciones.

El polimorfismo permite que objetos distintos respondan a nombre(), area()
y perimetro(): la función usa esos métodos sin conocer la clase concreta.
Cada figura es responsable de calcular su propia área y su perímetro.
Cuadrado hereda de Rectangulo porque es un rectángulo con lados iguales
y puede reutilizar sus cálculos. Como ofrece los mismos métodos, añadirlo
no requiere cambiar imprimir_informe().
"""

import math


def validar_medida(valor):
    """Comprueba que la medida sea int o float, positiva y no booleana."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError("La medida debe ser int o float, no un booleano.")
    if not valor > 0:
        raise ValueError("La medida debe ser mayor que 0.")


class Figura:
    def nombre(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Rectangulo(Figura):
    def __init__(self, base, altura):
        validar_medida(base)
        validar_medida(altura)
        self.base = base
        self.altura = altura

    def nombre(self):
        return "Rectángulo"

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, radio):
        validar_medida(radio)
        self.radio = radio

    def nombre(self):
        return "Círculo"

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class TrianguloRectangulo(Figura):
    def __init__(self, cateto1, cateto2):
        validar_medida(cateto1)
        validar_medida(cateto2)
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def nombre(self):
        return "Triángulo rectángulo"

    def area(self):
        return (self.cateto1 * self.cateto2) / 2

    def perimetro(self):
        return self.cateto1 + self.cateto2 + math.hypot(self.cateto1, self.cateto2)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def nombre(self):
        return "Cuadrado"


def imprimir_informe(figuras):
    for figura in figuras:
        print(
            figura.nombre(),
            round(figura.area(), 2),
            round(figura.perimetro(), 2)
        )


if __name__ == "__main__":
    figuras = [
        Rectangulo(3, 4),
        Circulo(2),
        TrianguloRectangulo(3, 4),
        Cuadrado(5),
    ]
    imprimir_informe(figuras)
