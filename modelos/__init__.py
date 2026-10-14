'''
El archivo __init__.py sirve para indicar que una carpeta está pensada para funcionar
como un paquete de Python. Además, permite ejecutar código de inicialización cuando
se importa ese paquete.

No hace nada, hace que desde /modelos/ pueda importar todas las clases de un tirón
'''

from .Libro import Libro
from .Usuario import Usuario
from .Prestamo import Prestamo

