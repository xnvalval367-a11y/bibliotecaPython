'''
id
nombre
apelllido
email
'''

class Usuario:

    def __init__(self, id, nombre, apellido, email):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.email=email

    #toString
    def __str__(self):
        return f"Usuario(nombre={self.nombre}, apellido={self.apellido}, email={self.email})"