'''
usuario
libro
fecha-prestamo
fecha-devolucion
'''
from .Libro import libro
from .Usuario import usuario
from datetime import date


class Prestamo:

    def __init__(self, libro: libro, usuario: usuario, fecha_prestamo, fecha_devolucion):
        self.libro=libro
        self.usuario=usuario
        self.fecha_prestamo=(fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion=fecha_devolucion


    '''
    quiero saber si el préstamo está vacío.Si fecha_devolución=None-> TRUE
    si fecha_devolucion != None -> FALSE

    El decorador @property en Python permite convertir un método de clase en un atributo
    de solo lectura o controlado, de modo que se accede a él sin necesidad de paréntesis 
    (por ejemplo, objeto.atributo en lugar de objeto.atributo())

    Permite leer el valor como si fuera un atributo común, pero ejecutando código por detrás
    '''
    @property
    def activo(self):
        return self.fecha_devolucion  is None


    #toString
    def __str__(self):
        return f"Prestamo(libro={self.libro.titulo}, usuario={self.usuario.nombre}, fecha de devolución= {self.fecha_devolucion})"
    