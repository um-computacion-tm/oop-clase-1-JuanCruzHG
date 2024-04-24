import unittest

class Alumno:
    def __init__(self, nombre, legajo, edad, email):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__email__ = email

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_legajo(self):
        return self.__legajo__

    def obtener_edad(self):
        return self.__edad__

    def obtener_email(self):
        return self.__email__

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class TestMateriaProfesor(unittest.TestCase):

    def test_materia_constructor(self):
        profesor = Profesor("Juan", "Profesor", "123")
        materia = Materia("Matemáticas", [profesor])
        self.assertEqual(materia.obtener_profesores(), [profesor])

    def test_profesor_constructor(self):
        profesor = Profesor("Juan", "Profesor", "123")
        self.assertEqual(profesor.obtener_nombre(), "Juan")
        self.assertEqual(profesor.obtener_cargo(), "Profesor")
        self.assertEqual(profesor.obtener_legajo(), "123")

    def test_alumno_constructor(self):
        alumno = Alumno("Ana", "A001", 20, "ana@example.com")
        self.assertEqual(alumno.obtener_nombre(), "Ana")
        self.assertEqual(alumno.obtener_legajo(), "A001")
        self.assertEqual(alumno.obtener_edad(), 20)
        self.assertEqual(alumno.obtener_email(), "ana@example.com")

    def test_materia_alumnos(self):
        materia = Materia("Matemáticas", [])
        alumno1 = Alumno("Ana", "A001", 20, "ana@example.com")
        alumno2 = Alumno("Juan", "A002", 22, "juan@example.com")
        materia.obtener_alumnos().extend([alumno1, alumno2])
        self.assertEqual(materia.obtener_alumnos(), [alumno1, alumno2])

    def test_materia_cambiar_nombre(self):
        materia = Materia("Matemáticas", [])
        materia.cambiar_nombre("Física")
        self.assertEqual(materia.__nombre__, "Física")

    def test_alumno_modificar_atributos(self):
        alumno = Alumno("Ana", "A001", 20, "ana@example.com")
        alumno.__nombre__ = "Juan"
        alumno.__legajo__ = "A002"
        alumno.__edad__ = 22
        alumno.__email__ = "juan@example.com"
        self.assertEqual(alumno.obtener_nombre(), "Juan")
        self.assertEqual(alumno.obtener_legajo(), "A002")
        self.assertEqual(alumno.obtener_edad(), 22)
        self.assertEqual(alumno.obtener_email(), "juan@example.com")

    def test_materia_profesores(self):
        profesor1 = Profesor("Juan", "Profesor", "123")
        profesor2 = Profesor("María", "Profesora", "456")
        materia = Materia("Matemáticas", [profesor1, profesor2])
        self.assertEqual(materia.obtener_profesores(), [profesor1, profesor2])

if __name__ == '__main__':
    unittest.main()
