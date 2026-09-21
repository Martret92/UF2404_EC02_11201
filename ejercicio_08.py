"""Respuestas del ejercicio 8.

1. Predicción antes de ejecutar — VERSIÓN ORIGINAL: class D(B, C).
   obj.metodo() mostrará DBCA. D.mro() devolverá las clases en este orden:
   D -> B -> C -> A -> object.

2. ¿Por qué?
   Python utiliza la MRO (Method Resolution Order / orden de resolución
   de métodos). Para D(B, C), la MRO es D -> B -> C -> A -> object.
   D llama al método de B mediante super(), B continúa hacia C y C
   continúa hacia A. A devuelve "A"; C devuelve "C" + "A" = "CA";
   B devuelve "B" + "CA" = "BCA"; y D devuelve "D" + "BCA" = "DBCA".
   A termina la cadena porque no llama a super().

3. Comprobación mediante ejecución.
   Al ejecutar python ejercicio_08.py, la primera parte muestra DBCA
   y la MRO D -> B -> C -> A -> object, confirmando la predicción.

4. VERSIÓN MODIFICADA: class D(C, B).
   Solo se invierte el orden de las bases de D; los métodos no cambian.
   La MRO pasa a ser D -> C -> B -> A -> object y el resultado es DCBA.
   La segunda parte permite comprobarlo con una nueva instancia de D.

5. ¿Qué hace realmente super()?
   No significa simplemente "llamar al padre de esta clase". Continúa
   buscando el método después de la clase donde se usa, según la MRO
   del objeto. En D(B, C), super() dentro de B encuentra C, aunque B
   hereda directamente de A. En D(C, B), después de C aparece B.
"""


# Primera parte: versión original del enunciado.
class A:
    def metodo(self):
        return "A"


class B(A):
    def metodo(self):
        return "B" + super().metodo()


class C(A):
    def metodo(self):
        return "C" + super().metodo()


class D(B, C):
    def metodo(self):
        return "D" + super().metodo()


if __name__ == "__main__":
    obj = D()
    print("VERSIÓN ORIGINAL: class D(B, C)")
    print("Resultado de obj.metodo():", obj.metodo())
    print("MRO de D:", D.mro())

    # Segunda parte: redefinimos D cambiando únicamente el orden de sus bases.
    class D(C, B):
        def metodo(self):
            return "D" + super().metodo()

    # Creamos otro objeto para utilizar la nueva definición de D.
    obj = D()
    print("\nVERSIÓN MODIFICADA: class D(C, B)")
    print("Resultado de obj.metodo():", obj.metodo())
    print("MRO de D:", D.mro())
