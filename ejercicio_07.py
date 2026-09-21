"""Sistema de cursos: herencia, composición y encapsulación.

Persona contiene el nombre común. Alumno y Profesor heredan de Persona
porque ambos son personas. Curso usa composición: contiene un Profesor
y objetos Alumno. Controla las matrículas comprobando tipo, duplicados
y capacidad máxima. La lista de alumnos se mantiene interna y se consulta
como tupla para no saltarse las reglas modificándola directamente.
__str__ permite obtener una representación legible del curso.
"""


class Persona:
    def __init__(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre.strip()

    def __str__(self):
        return self.nombre


class Alumno(Persona):
    """Un alumno es una persona y hereda sus datos y comportamiento."""


class Profesor(Persona):
    """Un profesor es una persona y hereda sus datos y comportamiento."""


class Curso:
    def __init__(self, nombre, profesor, capacidad_maxima):
        if not isinstance(nombre, str):
            raise TypeError("El nombre del curso debe ser un texto.")
        if not nombre.strip():
            raise ValueError("El nombre del curso no puede estar vacío.")
        if isinstance(capacidad_maxima, bool) or not isinstance(capacidad_maxima, int):
            raise TypeError("La capacidad máxima debe ser un entero, no un booleano.")
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.cambiar_profesor(profesor)
        self.capacidad_maxima = capacidad_maxima
        self._alumnos = []

    def obtener_alumnos(self):
        """Devuelve una tupla para no exponer la lista interna."""
        return tuple(self._alumnos)

    def matricular(self, alumno):
        if not isinstance(alumno, Alumno):
            raise TypeError("Solo se pueden matricular objetos Alumno.")
        if alumno in self._alumnos:
            raise ValueError("El alumno ya está matriculado.")
        if len(self._alumnos) >= self.capacidad_maxima:
            raise ValueError("El curso ha alcanzado su capacidad máxima.")
        self._alumnos.append(alumno)

    def desmatricular(self, alumno):
        if alumno not in self._alumnos:
            raise ValueError("El alumno no está matriculado.")
        self._alumnos.remove(alumno)

    def cambiar_profesor(self, profesor):
        if not isinstance(profesor, Profesor):
            raise TypeError("El profesor del curso debe ser un objeto Profesor.")
        self.profesor = profesor

    def __str__(self):
        alumnos = ", ".join(str(alumno) for alumno in self._alumnos)
        if not alumnos:
            alumnos = "Sin alumnos"
        return (
            f"Curso: {self.nombre}\n"
            f"Profesor: {self.profesor}\n"
            f"Alumnos: {alumnos}\n"
            f"Matriculados: {len(self._alumnos)} / {self.capacidad_maxima}"
        )


if __name__ == "__main__":
    profesora = Profesor("Laura")
    ana = Alumno("Ana")
    pablo = Alumno("Pablo")
    marta = Alumno("Marta")
    curso = Curso("Python", profesora, 2)

    print("Curso vacío:")
    print(curso)
    curso.matricular(ana)
    curso.matricular(pablo)
    print("\nDespués de matricular:")
    print(curso)

    try:
        curso.matricular(ana)
    except ValueError as error:
        print(f"\nMatrícula duplicada: {error}")

    try:
        curso.matricular(marta)
    except ValueError as error:
        print(f"Capacidad superada: {error}")

    try:
        curso.matricular("Luis")
    except TypeError as error:
        print(f"Tipo de alumno incorrecto: {error}")

    try:
        curso.cambiar_profesor(ana)
    except TypeError as error:
        print(f"Tipo de profesor incorrecto: {error}")

    curso.cambiar_profesor(Profesor("Carlos"))
    curso.desmatricular(ana)
    print("\nDespués de cambiar el profesor y desmatricular a Ana:")
    print(curso)
