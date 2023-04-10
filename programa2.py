#Importar programa 

#import programa1

#print(programa1.saludar("Johis"))
#user = programa1.Usuario("Johana", "johis99_@hotmail.es")
#print(user.nombre)

#Para importar una sola clase entonces se realiza el siguiente codigo, el anterior codigo es para importar todo el script del programa1.

from programa1 import Usuario

user = Usuario("Johana", "johis99_@hotmail.es")

#Solo para importar la clase no todo el script, como se puede ver

#Para llamar de otra carpeta que esta afuera de mi carpeta actual entonces se hace lo siguiente 
#Así se importa
#from .. import funciones

"""para importar librerias 
Para importar Random y math
"""

#from random import random
#Se importa la libreria math y se importa la función de raíz cuadrada
#from math import sqrt

#from random import *
# Para importar la librería se hace 
#import random
#random.


