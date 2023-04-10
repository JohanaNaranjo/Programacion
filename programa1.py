#Modulos y paquetes

nombre = "Johana"
edad = "21"

def saludar(nombre):
    return f"Hola {nombre}"

class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def premium(self):
        self.premium = True

