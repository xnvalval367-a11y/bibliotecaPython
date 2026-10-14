'''
isbn
titulo
autor
anio
genero
disponible
'''

class Libro:

    def __init__(self, isbn, titulo, autor, genero, anio=None, disponible=True):
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.anio=anio
        self.genero=genero
        self.disponible=disponible


    #toString
    def __str__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, anio={self.anio}, genero={self.genero}, disponible={self.disponible})"