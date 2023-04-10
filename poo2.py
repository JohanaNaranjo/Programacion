class Usuario:

    cantidad_usuarios =100

    def __init__(self, nombre, apellido, edad, persona_masculina):
        #Creando atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.persona_masculina = persona_masculina
        self.premium = False # Se utiliza en un apágina web sii se quiere crear una cuenta premium un usuario, no se deja que el usuario pueda cambiar su valor


    #Retrono de datos es siumiliar al str (string)
    def __repr__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad}, {self.persona_masculina}, {self.premium}"
    
    #Metodo para eliminar un atributo
    #def __delattr__(self, __name: str)

    #Metodo destructor elimina un objeto
    def __del__(self):
        print("Objeto borrado")

#Metodo para convertir usuario en premium
    def convertir_premium(self):
        self.premium = True

#Metodo para mirar peliculas premium
    def mirar_peliculas(self):
        if self.premium:
            print("El usuario puede ver las peliculas")
        else:
            print("El usuaio no es Premium")

#Metodo estatico
    @staticmethod
    def usuario_mayor(edad):
        return edad >= 18

#Metodo de clase
    @classmethod
    def catidad_usuarios(cls):
        return cls.cantidad_usuarios
    
usuario = Usuario("Johana", "Naranjo", "28", True)
print(usuario)
print(usuario.premium)
usuario.mirar_peliculas()
#Para convertir en premium
usuario.convertir_premium()
print(usuario)
print(usuario.premium)
usuario.mirar_peliculas()

#Para destruir objetos

del usuario
#Llamar el metodo estatico
print(Usuario.usuario_mayor(18))

#Usuario.cantidad_usuarios()
