
class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores

    def obtener_profesores(self):
        return self.__profesores__
    
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

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
    
class Alumno:
    def __init__(self, nombre, legajo, edad, email):
        self.__nombre__ = nombre
        self._legajo__ = legajo
        self.__edad__ = edad
        self.__email__ = email
        self.__inasistencias__ = 0
        self.__mentor__ = None

    def agregar_mentor(self, mentor):
        self.__mentor__ = mentor
    
    def cambiar_mail(self, email):
        self.__email__ = email

alumno = Alumno(nombre = 'camila', legajo = 62123, edad = 20, email = 'cami@gmail.com')
