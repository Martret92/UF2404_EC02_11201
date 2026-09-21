# UF2404 - EC02

Prueba práctica de la unidad formativa UF2404: Principios de la programación orientada a objetos.

## Ejercicios seleccionados

| Ejercicio | Archivo | Conceptos principales |
| --- | --- | --- |
| 3 | [ejercicio_03.py](ejercicio_03.py) | Polimorfismo, herencia |
| 5 | [ejercicio_05.py](ejercicio_05.py) | Polimorfismo, principio abierto/cerrado |
| 7 | [ejercicio_07.py](ejercicio_07.py) | Herencia, composición, encapsulación |
| 8 | [ejercicio_08.py](ejercicio_08.py) | Herencia múltiple, MRO, super() |
| 9 | [ejercicio_09.py](ejercicio_09.py) | Composición, encapsulación, relaciones entre objetos |

## Ejecución

Cada ejercicio es independiente. Desde la carpeta del repositorio, ejecuta el archivo correspondiente con Python:

```bash
python ejercicio_03.py
python ejercicio_05.py
python ejercicio_07.py
python ejercicio_08.py
python ejercicio_09.py
```

Dependiendo de la instalación de Windows, también puede utilizarse `py` en lugar de `python`.

## Resumen de los ejercicios

**Ejercicio 3.** La misma función trabaja con distintos tipos de figuras gracias al polimorfismo. `Cuadrado` reutiliza `Rectangulo`.

**Ejercicio 5.** `Pedido` delega el descuento en los objetos cliente, permitiendo añadir nuevos tipos sin modificar su lógica.

**Ejercicio 7.** `Persona` es la base de `Alumno` y `Profesor`. `Curso` utiliza composición y controla matrícula, capacidad y profesor.

**Ejercicio 8.** Demuestra cómo la MRO determina el comportamiento de `super()` en herencia múltiple y cómo cambia al invertir las bases de `D`.

**Ejercicio 9.** `Biblioteca` coordina libros, usuarios y préstamos. `Prestamo` relaciona objetos reales `Libro` y `Usuario` y controla el estado del préstamo.

## Conceptos de POO utilizados

- Herencia.
- Polimorfismo.
- Composición.
- Encapsulación.
- Reutilización de código.
- Gestión de errores mediante excepciones.
