"""Sistema de préstamos: explicación para la defensa.

Libro representa un libro y su disponibilidad; Usuario identifica al lector.
Prestamo relaciona los objetos Libro y Usuario y conserva su estado activo.
Guarda objetos para acceder a sus datos y compartir el mismo libro y usuario,
sin sustituirlos por nombres o identificadores aislados.
Biblioteca contiene libros, usuarios y préstamos (composición), coordina las
operaciones y mantiene sus colecciones internas por convención con el prefijo _.
El límite de tres se comprueba contando préstamos activos del mismo objeto
Usuario, sin mantener un contador redundante.
Al devolver, Biblioteca finaliza el préstamo y marca el libro como disponible.
El historial se conserva y prestamos_activos() devuelve una tupla nueva.
"""


class Libro:
    def __init__(self, isbn, titulo):
        if not isinstance(isbn, str) or not isinstance(titulo, str):
            raise TypeError("El ISBN y el título deben ser textos.")
        if not isbn.strip() or not titulo.strip():
            raise ValueError("El ISBN y el título no pueden estar vacíos.")
        self.isbn = isbn.strip()
        self.titulo = titulo.strip()
        self.disponible = True

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} (ISBN: {self.isbn}, {estado})"


class Usuario:
    def __init__(self, id_usuario, nombre):
        if not isinstance(id_usuario, str) or not isinstance(nombre, str):
            raise TypeError("El identificador y el nombre deben ser textos.")
        if not id_usuario.strip() or not nombre.strip():
            raise ValueError("El identificador y el nombre no pueden estar vacíos.")
        self.id_usuario = id_usuario.strip()
        self.nombre = nombre.strip()

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Prestamo:
    def __init__(self, libro, usuario):
        if not isinstance(libro, Libro) or not isinstance(usuario, Usuario):
            raise TypeError("Un préstamo necesita objetos Libro y Usuario.")
        self.libro = libro
        self.usuario = usuario
        self.activo = True

    def finalizar(self):
        self.activo = False

    def __str__(self):
        estado = "activo" if self.activo else "finalizado"
        return f"{self.libro.titulo} -> {self.usuario} ({estado})"


class Biblioteca:
    def __init__(self):
        self._libros = {}
        self._usuarios = {}
        self._prestamos = []

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se pueden agregar objetos Libro.")
        if libro.isbn in self._libros:
            raise ValueError("Ya existe un libro con ese ISBN.")
        self._libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Solo se pueden registrar objetos Usuario.")
        if usuario.id_usuario in self._usuarios:
            raise ValueError("Ya existe un usuario con ese identificador.")
        self._usuarios[usuario.id_usuario] = usuario

    def prestar(self, isbn, id_usuario):
        if isbn not in self._libros:
            raise ValueError("No existe un libro con ese ISBN.")
        if id_usuario not in self._usuarios:
            raise ValueError("No existe un usuario con ese identificador.")
        libro = self._libros[isbn]
        usuario = self._usuarios[id_usuario]
        if not libro.disponible:
            raise ValueError("El libro ya está prestado.")

        cantidad = sum(
            1 for prestamo in self._prestamos
            if prestamo.activo and prestamo.usuario is usuario
        )
        if cantidad >= 3:
            raise ValueError("El usuario ya tiene 3 préstamos activos.")

        prestamo = Prestamo(libro, usuario)
        libro.disponible = False
        self._prestamos.append(prestamo)
        return prestamo

    def devolver(self, isbn):
        if isbn not in self._libros:
            raise ValueError("No existe un libro con ese ISBN.")
        libro = self._libros[isbn]
        if libro.disponible:
            raise ValueError("El libro no está prestado.")
        for prestamo in self._prestamos:
            if prestamo.activo and prestamo.libro is libro:
                prestamo.finalizar()
                libro.disponible = True
                return
        raise ValueError("No se encuentra un préstamo activo para ese libro.")

    def prestamos_activos(self):
        return tuple(prestamo for prestamo in self._prestamos if prestamo.activo)


if __name__ == "__main__":
    biblioteca = Biblioteca()
    ana = Usuario("U1", "Ana")
    luis = Usuario("U2", "Luis")
    biblioteca.registrar_usuario(ana)
    biblioteca.registrar_usuario(luis)

    libros = [
        Libro("9780000000001", "El principito"),
        Libro("9780000000002", "Don Quijote"),
        Libro("9780000000003", "La isla del tesoro"),
        Libro("9780000000004", "Viaje al centro de la Tierra"),
    ]
    for libro in libros:
        biblioteca.agregar_libro(libro)

    primer_prestamo = biblioteca.prestar(libros[0].isbn, ana.id_usuario)
    biblioteca.prestar(libros[1].isbn, ana.id_usuario)
    biblioteca.prestar(libros[2].isbn, ana.id_usuario)
    print("Préstamos activos: Ana tiene 3")
    for prestamo in biblioteca.prestamos_activos():
        print(prestamo)

    # Cada error se captura aquí para que la demostración pueda continuar.
    try:
        biblioteca.registrar_usuario(Usuario("U1", "Otra persona"))
    except ValueError as error:
        print("\nIdentificador duplicado:", error)

    try:
        biblioteca.agregar_libro(Libro(libros[0].isbn, "Otro libro"))
    except ValueError as error:
        print("ISBN duplicado:", error)

    try:
        biblioteca.prestar(libros[0].isbn, luis.id_usuario)
    except ValueError as error:
        print("Libro ya prestado:", error)

    try:
        biblioteca.prestar(libros[3].isbn, ana.id_usuario)
    except ValueError as error:
        print("Cuarto préstamo simultáneo:", error)

    biblioteca.devolver(libros[0].isbn)
    print("\nDespués de devolver el primer libro:")
    print("Primer préstamo finalizado:", not primer_prestamo.activo)
    print("Libro disponible:", libros[0].disponible)
    for prestamo in biblioteca.prestamos_activos():
        print(prestamo)

    try:
        biblioteca.devolver(libros[0].isbn)
    except ValueError as error:
        print("\nDevolución repetida:", error)

    biblioteca.prestar(libros[3].isbn, ana.id_usuario)
    biblioteca.prestar(libros[0].isbn, luis.id_usuario)
    print("\nAna puede pedir otro libro tras devolver; Luis pide el devuelto:")
    for prestamo in biblioteca.prestamos_activos():
        print(prestamo)
