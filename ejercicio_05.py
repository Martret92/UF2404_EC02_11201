"""Ejercicio 5: refactorización mediante polimorfismo.

El código original obligaba a modificar Pedido al añadir tipos de cliente.
Pedido valida los datos, calcula el subtotal y delega el descuento al cliente.
Las clases de cliente indican su descuento y comparten la fórmula para aplicarlo.
Hay polimorfismo porque la misma llamada usa el descuento del objeto recibido.
ClienteEstudiante añade su descuento sin cambiar Pedido ni calcular_precio().
Así se cumple el principio abierto/cerrado: Pedido admite nuevos clientes
sin tener que modificar su código cada vez que aparece uno.
"""


class Cliente:
    def obtener_descuento(self):
        """Cada tipo de cliente debe indicar su descuento como fracción."""
        raise NotImplementedError("El cliente debe definir su descuento.")

    def aplicar_descuento(self, subtotal):
        return subtotal * (1 - self.obtener_descuento())


class ClienteNormal(Cliente):
    def obtener_descuento(self):
        return 0


class ClienteVIP(Cliente):
    def obtener_descuento(self):
        return 0.20


class Empleado(Cliente):
    def obtener_descuento(self):
        return 0.50


class ClientePremium(Cliente):
    def obtener_descuento(self):
        return 0.30


class Pedido:
    def calcular_precio(self, cliente, precio, cantidad):
        """Calcula el total usando el descuento del cliente recibido."""
        if isinstance(precio, bool) or not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor que 0.")
        # bool hereda de int en Python, pero no representa una cantidad válida.
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que 0.")

        subtotal = precio * cantidad
        return cliente.aplicar_descuento(subtotal)


# Nuevo tipo de cliente: no requiere cambiar la clase Pedido.
class ClienteEstudiante(Cliente):
    def obtener_descuento(self):
        return 0.15


if __name__ == "__main__":
    pedido = Pedido()
    precio = 100
    cantidad = 2

    clientes = [
        ("ClienteNormal", ClienteNormal()),
        ("ClienteVIP", ClienteVIP()),
        ("Empleado", Empleado()),
        ("ClientePremium", ClientePremium()),
        ("ClienteEstudiante", ClienteEstudiante()),
    ]

    for nombre, cliente in clientes:
        total = pedido.calcular_precio(cliente, precio, cantidad)
        print(f"{nombre}: {total:.2f}")
